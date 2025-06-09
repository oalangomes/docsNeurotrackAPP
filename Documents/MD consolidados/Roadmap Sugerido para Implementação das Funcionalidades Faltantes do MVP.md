# Roadmap Sugerido para Implementação das Funcionalidades Faltantes do MVP

Com base na análise comparativa (`analise_comparativa_backend_vs_consolidado_v3.md`) e na estrutura atual do backend, segue um caminho sugerido para implementar as funcionalidades essenciais restantes para o MVP do NeurotrackApp.

**Priorização Geral Sugerida:**
1.  **Segurança e Acesso:** Recuperação de Senha, Validação de E-mail.
2.  **Core Funcional (Diário e Tarefas):** Melhorias no Diário (Update, Campos Adicionais, Filtros, Privacidade), Gestão de Subtarefas via API.
3.  **Integrações Essenciais:** Conexão Tarefas -> Agenda.
4.  **Melhorias e Preparação Pós-MVP:** Registro de Uso de Medicação (base para Pós-MVP), Controle de Sincronização da Agenda.

---

## Detalhamento por Funcionalidade Faltante (MVP)

### 1. Recuperação de Senha

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Alta
*   **Etapas Sugeridas:**
    1.  **Endpoint Solicitação:** Criar `POST /auth/forgot-password` que recebe o e-mail do usuário.
    2.  **Lógica:** Verificar se o e-mail existe. Gerar um token de reset seguro (ex: JWT com expiração curta ou token aleatório armazenado com TTL no Redis/DB associado ao usuário).
    3.  **Envio de E-mail:** Integrar com um serviço de envio de e-mail (ex: SendGrid, Mailgun) para enviar um link contendo o token para o usuário.
    4.  **Endpoint Reset:** Criar `POST /auth/reset-password` que recebe o token e a nova senha.
    5.  **Lógica:** Validar o token (existência, expiração). Se válido, atualizar a senha do usuário no banco de dados e invalidar o token.
    6.  **Model:** Nenhuma mudança necessária no `User` schema inicialmente.

### 2. Validação de E-mail (Cadastro)

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Alta
*   **Etapas Sugeridas:**
    1.  **Model:** Adicionar um campo `isVerified: { type: Boolean, default: false }` e `verificationToken: String` ao `User` schema.
    2.  **Fluxo de Cadastro (`POST /auth/register`):** Após salvar o usuário, gerar um `verificationToken`, salvá-lo no usuário e enviar um e-mail de verificação (similar ao passo 3 da recuperação de senha) com um link contendo o token.
    3.  **Endpoint Verificação:** Criar `GET /auth/verify-email/:token`.
    4.  **Lógica:** Encontrar o usuário pelo token. Se encontrado, marcar `isVerified` como `true`, remover/invalidar o `verificationToken` e redirecionar/responder com sucesso.
    5.  **Middleware/Lógica de Acesso:** Impedir login (`POST /auth/login`) ou acesso a certas funcionalidades se `isVerified` for `false` (opcional, mas recomendado).

### 3. Diário: Atualizar Entrada

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Média
*   **Etapas Sugeridas:**
    1.  **Endpoint:** Criar `PATCH /dailyentries/:id`.
    2.  **Controller/Service:** Implementar lógica para encontrar a entrada pelo ID e usuário, atualizar os campos permitidos (texto, humor, etc.) e salvar.
    3.  **Validação:** Garantir que apenas o dono da entrada possa atualizá-la.

### 4. Diário: Suporte API para Campos Adicionais (Foco, Energia, Situação)

*   **Status Atual:** 🟡 Parcialmente Implementado (Modelo pode ter, API não expõe)
*   **Prioridade:** Média
*   **Etapas Sugeridas:**
    1.  **Model (`dailyEntry.js`):** Confirmar/Adicionar os campos: `focusLevel: Number`, `energyLevel: Number`, `situation: String` (com enum, ex: ["Reflexão", "Risco", "Pensamento Intrusivo", ...]).
    2.  **Endpoints:** Modificar `POST /dailyentries` e `PATCH /dailyentries/:id` para aceitar e validar esses novos campos no request body.
    3.  **Endpoints:** Modificar `GET /dailyentries` e `GET /dailyentries/:id` para retornar esses campos na resposta.
    4.  **Swagger:** Atualizar a documentação Swagger para refletir os novos campos.

### 5. Diário: Filtros de Histórico

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Média
*   **Etapas Sugeridas:**
    1.  **Endpoint:** Modificar `GET /dailyentries` para aceitar query parameters (ex: `?mood=4`, `?startDate=YYYY-MM-DD`, `?endDate=YYYY-MM-DD`, `?situation=Risco`).
    2.  **Controller/Service:** Implementar lógica para construir a query do MongoDB baseada nos parâmetros recebidos.
    3.  **Indexação:** Revisar índices no `dailyEntry.js` para otimizar consultas com filtros comuns.
    4.  **Swagger:** Atualizar documentação para incluir os query parameters de filtro.

### 6. Diário: Privacidade (Protegida/Sensível)

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Média (pode ser Alta dependendo dos requisitos de segurança)
*   **Etapas Sugeridas:**
    1.  **Model (`dailyEntry.js`):** Adicionar campos booleanos: `isProtected: { type: Boolean, default: false }`, `isSensitive: { type: Boolean, default: false }`.
    2.  **Endpoints:** Modificar `POST /dailyentries` e `PATCH /dailyentries/:id` para permitir definir esses flags.
    3.  **Lógica de Acesso:** Implementar lógica nos serviços/controllers para:
        *   Exigir autenticação extra (se `isProtected`) para visualização/edição (desafio: como implementar via API stateless? Talvez um endpoint `POST /dailyentries/:id/unlock` que valide senha/biometria e retorne um token de acesso temporário à entrada?).
        *   Impedir que entradas com `isSensitive` sejam enviadas para a IA (`POST /ai/generate-response`) ou retornadas em listagens gerais sem um filtro explícito.
    4.  **Serviço de IA:** Modificar `aiService` para verificar o flag `isSensitive` antes de processar o conteúdo.

### 7. Tarefas: Gestão de Subtarefas via API

*   **Status Atual:** 🟡 Parcialmente Implementado (Schema existe, API não expõe)
*   **Prioridade:** Média
*   **Etapas Sugeridas (Opção 1 - Modificar Endpoints Existentes):**
    1.  **Endpoints:** Modificar `POST /tasks` e `PATCH /tasks/:id` para aceitar/atualizar o array `breakdown` no request body.
    2.  **Validação:** Implementar validação para os dados das subtarefas recebidas.
    3.  **Controller/Service:** Ajustar a lógica para manipular o array `breakdown` (adicionar, remover, atualizar subtarefas).
*   **Etapas Sugeridas (Opção 2 - Endpoints Dedicados):**
    1.  **Endpoints:** Criar endpoints específicos para subtarefas: `POST /tasks/:taskId/breakdown`, `PATCH /tasks/:taskId/breakdown/:subtaskId`, `DELETE /tasks/:taskId/breakdown/:subtaskId`.
    2.  **Controller/Service:** Implementar a lógica para cada operação, interagindo com o array `breakdown` da tarefa pai.
    3.  **Swagger:** Documentar os novos endpoints ou as modificações nos existentes.
    *   *Recomendação:* Opção 2 pode ser mais clara e granular para o frontend.

### 8. Tarefas: Suporte API para Nível de Energia

*   **Status Atual:** 🟡 Parcialmente Implementado (Modelo tem, API não expõe)
*   **Prioridade:** Baixa (dentro do MVP)
*   **Etapas Sugeridas:**
    1.  **Model (`task.js`):** Confirmar campo `energyLevelRequired: Number`.
    2.  **Endpoints:** Modificar `POST /tasks` e `PATCH /tasks/:id` para aceitar e validar `energyLevelRequired`.
    3.  **Endpoints:** Modificar `GET /tasks` e `GET /tasks/:id` para retornar o campo.
    4.  **Swagger:** Atualizar documentação.

### 9. Agenda: Conexão Tarefas -> Agenda

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Média
*   **Etapas Sugeridas:**
    1.  **Gatilho:** Identificar o momento de criar/atualizar o evento no Google Calendar (ex: na criação/atualização da tarefa via `POST /tasks` ou `PATCH /tasks/:id` se `dueDate` tiver hora definida).
    2.  **Serviço (`taskService.js`):** Após salvar a tarefa, verificar se ela deve ir para a agenda. Se sim, chamar o `googleCalendarService.js`.
    3.  **Serviço (`googleCalendarService.js`):** Criar/Adaptar função para receber dados da tarefa e criar/atualizar um evento correspondente no Google Calendar (requer token do usuário).
    4.  **Model (`task.js`):** Adicionar campo `googleCalendarEventId: String` para armazenar o ID do evento criado no Google e facilitar updates/deletes.
    5.  **Lógica de Sincronização:** Lidar com atualizações e exclusões de tarefas, refletindo as mudanças no Google Calendar.
    6.  **Interface:** Considerar um flag opcional na criação/edição da tarefa: "Adicionar ao Google Agenda?".

### 10. Agenda: Privacidade/Controle Sincronização

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Baixa (dentro do MVP, mas importante para Pós-MVP)
*   **Etapas Sugeridas:**
    1.  **Model (`User.js`):** Adicionar campos para armazenar o status da sincronização (ex: `googleCalendarSyncEnabled: Boolean`) e talvez preferências (ex: quais tipos de tarefas sincronizar).
    2.  **Endpoints:** Criar `PATCH /users/me/settings/calendar` para permitir ao usuário ativar/desativar a sincronização e definir preferências.
    3.  **Lógica:** Serviços (`taskService`, `agendaService`) devem verificar esses settings antes de tentar sincronizar.

### 11. Medicação: Registro de Uso

*   **Status Atual:** ❌ Não Implementado
*   **Prioridade:** Baixa (Preparação Pós-MVP)
*   **Etapas Sugeridas:**
    1.  **Model (`medication.js`):** Adicionar um array para histórico de uso, similar ao `completionHistory` das tarefas: `usageHistory: [{ date: Date, status: String }]` (status: 'taken', 'skipped', 'skipped_sideeffect').
    2.  **Endpoint:** Criar `POST /medications/:id/log` para registrar uma ocorrência (tomada ou pulada).
    3.  **Controller/Service:** Implementar lógica para adicionar a entrada ao `usageHistory`.

---

Este roadmap fornece uma direção. A ordem exata e a complexidade podem variar dependendo das decisões de arquitetura e da capacidade da equipe. Recomenda-se quebrar essas implementações em histórias de usuário menores e iterar sobre elas.
