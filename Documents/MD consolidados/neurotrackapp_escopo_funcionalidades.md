# NeurotrackApp - Funcionalidades Mapeadas

## Escopo do MVP

### 1. Cadastro e Perfil
- Cadastro de usuário com e-mail/senha e login via Google
- Tela de preenchimento de dados complementares após o cadastro
- Campos condicionais com lógica de exibição dinâmica:
  - Campo “Estágio” só aparece se o diagnóstico for selecionado
  - Campo “Neurodivergente?” é inferido automaticamente
- Tela de resumo final do cadastro

### 2. Entrada Diária (Journaling)
- Registro de entrada com nota/texto diário
- Análise semântica do texto com IA (OpenAI)
- Sugestão automática de tarefas e mensagem de acolhimento com base nas entradas

### 3. Gerenciamento de Tarefas
- Criação de tarefas com título, descrição e data
- Suporte a quebra de tarefas (subtarefas)
- Status, prioridade, tags sensoriais e histórico de execução
- Preferências neurodivergentes aplicadas (ex: duração ideal, buffer de tempo)

### 4. Chat IA Personalizado
- Chat inteligente com IA adaptado ao perfil neurodivergente do usuário
- Contextualização automática com preferências e perfil
- Histórico com cache semântico por prompt/contexto

### 5. Resumo Final e Home
- Exibição de resumo diário com tarefas, sugestões e mensagem de IA
- Interface limpa e acessível
- Mensagens personalizadas por perfil

---

## Funcionalidades Pós-MVP

### 6. Integração com Agenda
- Sincronização com Google Calendar
- Criação e exclusão de eventos na agenda
- Agendamento de tarefas no calendário

### 7. Gestão de Medicação
- Registro de medicamentos, horários e posologia
- Lembretes para o usuário
- Registro de efeitos percebidos (futuro)

### 8. Preferências Avançadas
- Customização de alertas sensoriais (visual, auditivo, háptico)
- Estratégias de produtividade baseadas no perfil
- Contextos adaptativos por momento do dia (ex: manhã = foco)

### 9. Configurações de Segurança e Conta
- Atualização de e-mail e redefinição de senha
- Autenticação multifator (futuro)
- Exclusão lógica do usuário (soft delete)

### 10. Análises e Relatórios
- Resumo de uso com gráficos e insights
- Análise de evolução emocional e de tarefas
- Relatório PDF exportável

---

## Observações Técnicas
- Backend em Node.js com Express e MongoDB
- Testes com Jest e Supertest
- Middleware com cache semântico, análise contextual, tagging automático e TTL inteligente
- Integração com Redis para cache e histórico
- Swagger gerado automaticamente via controllers
- Padrão visual validado com contrastes acessíveis e inputs otimizados
- Uso planejado de embeddings para sugestão contextual futura