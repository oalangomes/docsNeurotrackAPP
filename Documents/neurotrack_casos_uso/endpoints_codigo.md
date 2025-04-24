# Endpoints do NeuroTrack - Documentação Extraída do Código

## 1. Autenticação (Auth)

### Endpoints de Autenticação
- **POST /auth/register** - Registra um novo usuário
- **POST /auth/login** - Autentica um usuário existente
- **POST /auth/google-login** - Login via Google
- **POST /auth/logout** - Encerra a sessão do usuário

## 2. Entradas Diárias (Daily Entries)

### Endpoints de Entradas Diárias
- **POST /dailyentries** - Cria uma nova entrada diária
- **GET /dailyentries** - Lista todas as entradas diárias do usuário
- **GET /dailyentries/:id** - Obtém uma entrada diária específica
- **DELETE /dailyentries/:id** - Remove uma entrada diária

## 3. Inteligência Artificial (AI)

### Endpoints de IA
- **POST /ai/generate-response** - Gera uma resposta usando IA
- **POST /ai/summarize-tasks** - Sumariza tarefas usando IA
- **POST /ai/feedback** - Salva feedback do usuário sobre resposta da IA
- **GET /ai/history** - Lista histórico de interações com IA

## 4. Tarefas (Tasks)

### Endpoints de Tarefas
- **POST /tasks** - Cria uma nova tarefa
- **GET /tasks** - Lista todas as tarefas do usuário
- **GET /tasks/:id** - Obtém uma tarefa específica
- **PATCH /tasks/:id** - Atualiza uma tarefa
- **DELETE /tasks/:id** - Remove uma tarefa

## 5. Calendário/Agenda

### Endpoints de Calendário
- **POST /calendar/events** - Cria um novo evento de agenda
- **GET /calendar/events** - Lista eventos do usuário
- **PATCH /calendar/events/:id** - Atualiza um evento
- **DELETE /calendar/events/:id** - Remove um evento
- **GET /calendar/google/auth** - Redireciona para autenticação do Google
- **GET /calendar/google/callback** - Finaliza o login OAuth do Google
- **POST /calendar/sync** - Sincroniza evento local com Google Calendar

## 6. Medicações

### Endpoints de Medicações
- **POST /medications** - Cria uma nova medicação
- **PATCH /medications/:id** - Atualiza uma medicação
- **DELETE /medications/:id** - Remove uma medicação

## 7. Saúde da API (Health)

### Endpoints de Monitoramento
- **GET /health** - Verifica a saúde da API

## 8. Usuários (Users)

### Endpoints de Usuários
- **GET /users/me** - Obtém o perfil do usuário autenticado
- **PATCH /users/me** - Atualiza o perfil do usuário autenticado
- **PATCH /users/me/preferences** - Atualiza as preferências do usuário
- **PATCH /users/password** - Atualiza a senha do usuário
- **PATCH /users/me/neuro-profile** - Atualiza o perfil neurodivergente do usuário
- **DELETE /users/me** - Deleta a conta do usuário autenticado
