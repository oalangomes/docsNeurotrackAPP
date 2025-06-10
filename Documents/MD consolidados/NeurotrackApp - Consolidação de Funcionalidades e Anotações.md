# NeurotrackApp - Consolidação de Funcionalidades e Anotações

## Introdução

Este documento consolida o escopo funcional e as anotações técnicas relevantes para o projeto NeurotrackApp, compilados a partir de diversos arquivos de escopo fornecidos. O objetivo é apresentar uma visão unificada das funcionalidades planejadas para o Produto Mínimo Viável (MVP) e fases posteriores (Pós-MVP), além de registrar decisões de arquitetura, tecnologias, padrões de interface e planos futuros.


## ✅ MVP - Funcionalidades Essenciais Consolidadas

Esta seção agrupa as funcionalidades consideradas essenciais para o Produto Mínimo Viável (MVP) do NeurotrackApp, conforme identificado nos diversos documentos de escopo.

### 1. Cadastro, Autenticação e Perfil do Usuário

- **Criação de Conta:** Permitir cadastro utilizando e-mail e senha, com validações adequadas. Suporte também para login social via Google (OAuth).
- **Autenticação:** Implementar login seguro utilizando JSON Web Tokens (JWT) para proteger endpoints da API.
- **Preenchimento de Perfil Complementar:** Após o cadastro inicial, solicitar informações adicionais como nome, idade/data de nascimento, idioma, gênero (opcional).
- **Perfil Neurodivergente:** Coletar informações sobre diagnósticos (ex: TDAH, TEA), sintomas e estágio (este último visível apenas se um diagnóstico for selecionado).
- **Detecção Automática:** Inferir automaticamente o status "Neurodivergente?" e o "Tipo de Perfil" com base nos dados fornecidos (lógica no backend).
- **Gestão de Dependentes:** Permitir vincular responsáveis e dependentes (para cenários de uso por pais/responsáveis).
- **Resumo Final:** Apresentar uma tela de resumo ao final do processo de cadastro/perfil.
- **Segurança da Conta (MVP inicial):** Incluir funcionalidades básicas como logout.

### 2. Entrada Diária (Journaling)

- **Registro Diário:** Permitir que o usuário registre eventos, humor (possivelmente com emojis selecionáveis), foco, energia, reflexões, sentimentos ou desabafos do dia. Armazenar com timestamp e ID do usuário.
- **Histórico:** Possibilitar a visualização do histórico de entradas diárias, listadas por data.
- **Sugestões da IA:** Integrar com IA (OpenAI) para fornecer sugestões automáticas (respostas, tarefas, mensagens de acolhimento) com base no texto inserido e no histórico do usuário. Realizar análise semântica/sentimentos simples.
- **Privacidade:** Garantir criptografia dos dados registrados e exibir avisos de privacidade na interface.

### 3. Gerenciamento de Tarefas

- **CRUD Completo:** Permitir a criação, visualização, edição e exclusão de tarefas.
- **Campos da Tarefa:** Incluir título, descrição, data de vencimento/início/fim, prioridade, status (pendente, em progresso, concluída, arquivada), tags sensoriais e nível de energia necessário.
- **Quebra de Tarefas:** Oferecer a opção de dividir tarefas complexas em subtarefas (implementado via modal ou flag `breakdown`).
- **Marcação de Conclusão:** Permitir marcar tarefas como concluídas.
- **Visualização:** Listar tarefas por dia, agrupadas por status ou data.
- **Sugestões da IA:** Utilizar IA para resumir tarefas (`/ai/summarize-tasks`), sugerir foco e organização com base no perfil, contexto e preferências neurodivergentes (duração ideal, buffer de tempo).
- **Interface Padronizada:** Utilizar modais de criação/edição com layout validado (inputs de linha única, ícones azuis).
- **Designação Futura:** Backend preparado para futura designação de tarefas a outros usuários (`assignedTo`).

### 4. Chat IA Personalizado

- **Interface de Chat:** Disponibilizar uma tela de chat (estilo bolha) para interação direta com o assistente virtual (IA).
- **Integração com OpenAI:** Utilizar a API da OpenAI para processar as mensagens e gerar respostas.
- **Contextualização:** Adaptar as respostas da IA com base no perfil do usuário (diagnósticos, preferências), histórico de registros e contexto da conversa (mantido por sessão).
- **Histórico:** Manter o histórico das conversas por usuário (armazenamento local e/ou backend).
- **Feedback Visual:** Exibir indicador de "digitando..." enquanto a IA processa a resposta.
- **Middleware Inteligente (MVP inicial):** Implementar cache básico (Redis) para prompts/respostas e histórico por usuário. Estrutura preparada para evoluções (tagging, similaridade, TTL adaptativo).

### 5. Integração com Agenda (Google Calendar)

- **CRUD de Eventos Locais:** Permitir a criação, visualização, edição e exclusão de eventos diretamente no aplicativo.
- **Sincronização com Google Calendar:** Implementar integração via OAuth2 para sincronizar eventos (criação, atualização, exclusão) entre o app e a agenda do Google do usuário. Armazenar token de forma segura e utilizar UIDs para mapeamento.
- **Visualização:** Exibir eventos da agenda na interface do app.

### 6. Tela Home e Resumo Final

- **Dashboard Diário:** Apresentar uma tela inicial (Home) com um resumo visual do dia, incluindo tarefas pendentes, última entrada diária, eventos da agenda e sugestões da IA.
- **Navegação:** Oferecer acesso rápido às principais funcionalidades (Chat, Tarefas, Diário).
- **Interface:** Manter um layout limpo, acessível e intuitivo, com mensagens personalizadas pela IA com base no perfil.




## 🔄 Pós-MVP - Funcionalidades Complementares e Futuras

Esta seção detalha as funcionalidades planejadas para fases posteriores ao MVP, incluindo melhorias, novas integrações e capacidades avançadas.

### 7. Gestão de Medicação
- **CRUD de Medicações:** Permitir o cadastro, edição e exclusão de medicamentos, incluindo nome, dose, horários e frequência.
- **Lembretes:** Configurar lembretes visuais e/ou notificações para a tomada de medicação.
- **Registro de Uso:** Possibilitar marcar a medicação como tomada (check).
- **Histórico e Relatórios:** Visualizar histórico de adesão e, futuramente, gerar relatórios de adesão.
- **Integração com Diário:** Futuramente, permitir relacionar a tomada de medicação com efeitos percebidos registrados na entrada diária.

### 8. Preferências Avançadas e Personalização
- **Ajustes da IA:** Permitir que o usuário ajuste o comportamento da IA (tom de voz, estilo de resposta - curta, empática, técnica, linguagem).
- **Configurações de Perfil:** Expandir as preferências para incluir estilo de aprendizado, sensibilidades sensoriais, preferências de rotina, filtros para sugestões.
- **Temas Visuais:** Oferecer opções de tema (Claro, Escuro, Sistema) e complexidade visual (Mínima, Média).
- **Alertas e Feedback:** Configurar alertas sonoros (Suaves, Nenhum) e feedback tátil.
- **Contextos Adaptativos:** Futuramente, adaptar a interface ou sugestões com base no momento do dia (ex: manhã = foco).

### 9. Configurações de Segurança e Conta
- **Recuperação de Senha:** Implementar fluxo completo de redefinição de senha (solicitação, confirmação via e-mail/modal).
- **Atualização de Dados:** Permitir a atualização do e-mail associado à conta.
- **Termos de Uso:** Apresentar modal para aceite dos termos de uso.
- **Autenticação Multifator (MFA):** Planejado para futuras versões.
- **Exclusão de Conta:** Oferecer opção para deletar a conta (exclusão lógica/soft delete inicialmente).

### 10. Análises, Relatórios e Estatísticas
- **Dashboards Pessoais:** Apresentar visualizações gráficas (humor, foco, energia, tarefas concluídas) por período (semanal/mensal).
- **Insights da IA:** Gerar insights automáticos com base nos registros e padrões identificados.
- **Exportação:** Permitir a exportação de dados e relatórios em formatos como CSV, JSON ou PDF (relatórios mensais para responsáveis ou terapeutas).
- **Comparativos:** Exibir comparativo de tarefas concluídas por semana.

### 11. Rotinas e Hábitos
- **Criação de Rotinas:** Permitir a definição de rotinas visuais (diárias/semanais).
- **Checklist de Hábitos:** Implementar funcionalidade para acompanhar hábitos diários.
- **Integração:** Conectar rotinas com lembretes, tarefas e agenda.
- **Gamificação (Streak):** Incluir reforço positivo para manutenção de rotinas e hábitos (streaks).

### 12. Gamificação e Engajamento
- **Sistema de Pontos:** Implementar sistema de pontos e conquistas por consistência e conclusão de tarefas.
- **Recompensas:** Oferecer medalhas, feedbacks positivos ou avatares desbloqueáveis.
- **Desafios:** Incluir desafios semanais propostos pela IA.
- **Modo Imersivo:** Oferecer um modo de foco com sons, timers e modo escuro.

### 13. Compartilhamento e Colaboração
- **Acesso Multiusuário:** Permitir que responsáveis acessem e gerenciem perfis de dependentes (crianças).
- **Compartilhamento com Profissionais:** Possibilitar o compartilhamento seguro de dados (registros, relatórios) com terapeutas ou familiares (via chave ou token).
- **Planos de Atividades:** Futuramente, permitir criar e compartilhar planos de atividades customizados com outros usuários ou acessar um repositório.

### 14. Integrações Adicionais
- **Microsoft Calendar:** Integrar com a API do Microsoft Graph.
- **Alexa:** Desenvolver uma Skill para interação via Alexa.
- **Apple Calendar/Health, Google Fit, Wearables:** Sincronizar com outros serviços de saúde e dispositivos vestíveis.
- **Notificações Push:** Utilizar FCM para notificações avançadas e preditivas.
- **Geolocalização:** Usar localização para lembretes contextuais (futuro).




## ⚙️ Anotações Técnicas e Observações Consolidadas

Esta seção reúne observações técnicas, decisões de arquitetura, tecnologias, padrões de UI/UX e outros detalhes relevantes mencionados nos documentos de escopo.

### Tecnologias Principais
- **Backend:** Node.js com Express.js.
- **Frontend:** React Native.
- **Banco de Dados:** MongoDB (utilizando Mongoose como ODM). `MongoMemoryServer` é usado para testes automatizados.
- **Cache:** Redis é utilizado extensivamente para cache de prompts da IA, histórico de usuário, controle de sessão e rate limiting. Estratégias de TTL (Time-To-Live) fixas e adaptativas são mencionadas, com planos para cache inteligente e invalidação baseada em semântica (embeddings).
- **Inteligência Artificial:** Integração primária com a API da OpenAI (GPT-3.5/GPT-4). Planos futuros incluem a exploração de modelos open-source (LLama 3, Mistral via Hugging Face/Ollama) e, eventualmente, o treinamento de um modelo próprio com dados do app.

### Arquitetura e Padrões de Backend
- **Estrutura:** Arquitetura modular com separação clara entre `controllers`, `services` e `middlewares`.
- **Autenticação:** Baseada em JWT para proteger rotas da API.
- **Validação:** Uso da biblioteca Joi para validação de entradas (payloads de requisição, variáveis de ambiente), com suporte a mensagens de erro multilíngue centralizadas (`messages.js`).
- **API:** Design RESTful. API Gateway mencionado para controle de rotas e middlewares.
- **Middleware da IA:** Um middleware robusto para interações com a IA é frequentemente descrito, incluindo funcionalidades como cache inteligente (verificando similaridade com prompts anteriores via Redis e NLP/embeddings), tagging automático de prompts, context awareness (perfil, histórico, horário), histórico por usuário e fallback para contexto inválido. Planos incluem filas de background (BullMQ) para respostas lentas.
- **Logs:** Sistema de logging estruturado (Pino/Winston mencionados), com categorias (erro, info, debug) e IDs de correlação.
- **Segurança:** Implementação de Helmet, CORS, rate limiting (por endpoint/usuário via Redis) e sanitização de inputs.
- **Configuração:** Suporte a múltiplos ambientes via arquivos `.env`.
- **Suporte a Módulos ES:** Projeto configurado para usar `type: "module"`.

### Testes e Qualidade
- **Ferramentas:** Jest para testes unitários e Supertest para testes de API/integração.
- **Cobertura:** Metas de cobertura de testes mencionadas (mínimo 65%, idealmente >90%), com relatórios automáticos (ex: Codecov).
- **Mocks:** Uso de `jest.unstable_mockModule` para mockar dependências.
- **CI/CD:** Pipelines de Integração Contínua (GitHub Actions) configurados para rodar testes automaticamente, com simulação de serviços (Redis, MongoDB). Proteção da branch `master` (testes obrigatórios, reviewers).
- **Segurança de Dependências:** Uso do Dependabot para atualizações automáticas de segurança.

### Interface e Experiência do Usuário (UI/UX)
- **Foco em Neurodivergência:** Layout projetado para ser limpo, intuitivo e acessível, considerando necessidades de usuários neurodivergentes (TDAH, TEA).
- **Padrões Visuais:** Validação de um guia de estilo UI/UX. Elementos padronizados incluem inputs com bordas suaves, ícones azuis, campos de linha única, SelectBoxes com seta padrão, botão "Cancelar" com fundo branco e borda. Paleta de cores e contrastes validados para acessibilidade.
- **Componentes:** Modais padronizados para criação/edição (tarefas, medicação, etc.).
- **Feedback:** Uso de indicadores visuais (ex: "digitando..." no chat), animações e reforços positivos.

### Documentação
- **API:** Geração automática de documentação Swagger (OpenAPI 3.0) a partir de anotações (`@swagger`) nas rotas, incluindo exemplos por endpoint. Disponibilização via endpoint `/api-docs` e exportação JSON. Geração de documentação em Markdown para GitHub também mencionada.
- **Arquitetura:** Planejamento de uso de diagramas C4 e BPMN para documentar a arquitetura e fluxos.

### Infraestrutura
- **Containerização:** Uso de Docker para integrar a aplicação, Redis e MongoDB.
- **Monitoramento:** Planos para implementar monitoramento com ElasticStack ou Loki/Grafana.
- **Healthcheck:** Endpoint de verificação de saúde da aplicação.

### Observações Gerais do Projeto
- **Equipe:** Mencionado como sendo desenvolvido por uma única pessoa exercendo múltiplos papéis (GP, Dev, QA).
- **Esforço/Orçamento:** Estimativas iniciais de 10h/semana por ~30 semanas para o MVP, com orçamento limitado (foco em ferramentas gratuitas/open-source).
- **Multilíngue:** Suporte planejado para Português (`pt`) e Inglês (`en`).

## Referências

Esta consolidação foi baseada nos seguintes arquivos:
- Escopo_NeurotrackApp (4).md
- Escopo_NeurotrackApp_MVP_PósMVP.md
- NeurotrackApp_Escopo.md
- escopo_neurotrackApp (2).md
- escopo_neurotrackApp (3).md
- escopo_neurotrackApp.md
- escopo_neurotrack_mvp_pos.md
- escopo_neurotrackapp (1).md
- escopo_neurotrackapp_mvp_pos_mvp.md
- neurotrack_escopo (1).md
- neurotrack_escopo.md
- neurotrack_escopo_funcional.md
- neurotrackapp_escopo_funcionalidades.md

*(Arquivos como central-estudos-completo.md e central-estudos-template.md foram ignorados por não serem relevantes ao escopo do NeurotrackApp)*

