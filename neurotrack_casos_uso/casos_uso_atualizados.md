# NeurotrackApp - Casos de Uso e Cenários de Teste

## Versão 2.0 | Abril 2025

## Sumário

1. [Introdução](#introdução)
2. [Visão Geral do Sistema](#visão-geral-do-sistema)
3. [Casos de Uso](#casos-de-uso)
   - [Autenticação e Perfil](#autenticação-e-perfil)
   - [Entradas Diárias](#entradas-diárias)
   - [Gerenciamento de Tarefas](#gerenciamento-de-tarefas)
   - [Inteligência Artificial](#inteligência-artificial)
   - [Gestão de Medicação](#gestão-de-medicação)
   - [Integração com Agenda](#integração-com-agenda)
   - [Monitoramento de Saúde da API](#monitoramento-de-saúde-da-api)
4. [Cenários de Teste](#cenários-de-teste)
5. [Modelos de Dados](#modelos-de-dados)
6. [Diagramas de Fluxo](#diagramas-de-fluxo)

## Introdução

O NeurotrackApp é um assistente digital projetado para ajudar pessoas neurodivergentes (TDAH, TEA) ou com dificuldades de produtividade e organização. Este documento apresenta os casos de uso e cenários de teste atualizados, refletindo a implementação atual do sistema.

## Visão Geral do Sistema

O NeurotrackApp oferece suporte com:
- Lembretes de medicamentos, consultas e tarefas
- Registro emocional e comportamental
- Análise de padrões via IA
- Divisão de tarefas em etapas menores
- Linha do tempo de evolução
- Integração com Google Calendar

### Tecnologias
- Backend: Node.js
- Frontend: React Native
- Banco de dados: MongoDB
- IA: OpenAI
- Autenticação: JWT
- Cache: Redis

## Casos de Uso

### Autenticação e Perfil

#### 1. Cadastro de Usuário
- **Endpoint**: POST /auth/register
- **Descrição**: Permite que um novo usuário crie uma conta no sistema
- **Parâmetros**:
  - auth.local.email: Email do usuário
  - auth.local.password: Senha do usuário
  - profile.name: Nome do usuário
  - profile.age: Idade do usuário
  - neuroProfile: Informações sobre o perfil neurodivergente (opcional)
  - preferences: Preferências do usuário (opcional)
  - system.lang: Idioma do sistema (opcional)
- **Resposta**: Token JWT para autenticação

#### 2. Login de Usuário
- **Endpoint**: POST /auth/login
- **Descrição**: Autentica um usuário existente
- **Parâmetros**:
  - email: Email do usuário
  - password: Senha do usuário
- **Resposta**: Token JWT para autenticação

#### 3. Login via Google
- **Endpoint**: POST /auth/google-login
- **Descrição**: Permite autenticação usando conta Google
- **Parâmetros**:
  - google_token: Token de autenticação do Google
- **Resposta**: Token JWT para autenticação

#### 4. Logout
- **Endpoint**: POST /auth/logout
- **Descrição**: Encerra a sessão do usuário
- **Parâmetros**: Nenhum
- **Resposta**: Confirmação de logout bem-sucedido

#### 5. Obter Perfil do Usuário
- **Endpoint**: GET /users/me
- **Descrição**: Retorna informações do perfil do usuário autenticado
- **Parâmetros**: Nenhum
- **Resposta**: Dados do perfil do usuário

#### 6. Atualizar Perfil do Usuário
- **Endpoint**: PATCH /users/me
- **Descrição**: Atualiza informações do perfil do usuário
- **Parâmetros**:
  - name: Nome do usuário (opcional)
  - age: Idade do usuário (opcional)
  - email: Email do usuário (opcional)
- **Resposta**: Perfil atualizado

#### 7. Atualizar Preferências
- **Endpoint**: PATCH /users/me/preferences
- **Descrição**: Atualiza preferências do usuário
- **Parâmetros**:
  - style: Estilo de interação (ex: "motivacional")
  - lang: Idioma (ex: "pt")
  - themes: Temas de interesse (ex: ["foco", "relaxamento"])
- **Resposta**: Preferências atualizadas

#### 8. Atualizar Senha
- **Endpoint**: PATCH /users/password
- **Descrição**: Permite que o usuário altere sua senha
- **Parâmetros**:
  - currentPassword: Senha atual
  - newPassword: Nova senha
- **Resposta**: Confirmação de senha atualizada

#### 9. Atualizar Perfil Neurodivergente
- **Endpoint**: PATCH /users/me/neuro-profile
- **Descrição**: Atualiza informações sobre o perfil neurodivergente do usuário
- **Parâmetros**:
  - type: Tipo de neurodivergência
  - diagnoses: Lista de diagnósticos
  - symptoms: Lista de sintomas
  - medicationSchedule: Agenda de medicações
- **Resposta**: Perfil neurodivergente atualizado

#### 10. Deletar Conta
- **Endpoint**: DELETE /users/me
- **Descrição**: Remove permanentemente a conta do usuário
- **Parâmetros**: Nenhum
- **Resposta**: Confirmação de conta deletada

### Entradas Diárias

#### 11. Criar Entrada Diária
- **Endpoint**: POST /dailyentries
- **Descrição**: Registra uma nova entrada diária com humor e texto
- **Parâmetros**:
  - text: Texto da entrada
  - date: Data da entrada
  - mood: Nível de humor (1-5)
- **Resposta**: Entrada criada com ID

#### 12. Listar Entradas Diárias
- **Endpoint**: GET /dailyentries
- **Descrição**: Retorna todas as entradas diárias do usuário
- **Parâmetros**: Nenhum
- **Resposta**: Lista de entradas diárias

#### 13. Obter Entrada Diária
- **Endpoint**: GET /dailyentries/:id
- **Descrição**: Retorna uma entrada diária específica
- **Parâmetros**:
  - id: ID da entrada
- **Resposta**: Detalhes da entrada diária

#### 14. Deletar Entrada Diária
- **Endpoint**: DELETE /dailyentries/:id
- **Descrição**: Remove uma entrada diária
- **Parâmetros**:
  - id: ID da entrada
- **Resposta**: Confirmação de remoção

### Gerenciamento de Tarefas

#### 15. Criar Tarefa
- **Endpoint**: POST /tasks
- **Descrição**: Cria uma nova tarefa
- **Parâmetros**:
  - title: Título da tarefa
  - description: Descrição da tarefa (opcional)
  - dueDate: Data de vencimento (opcional)
  - priority: Prioridade (1-5) (opcional)
  - sensoryTags: Tags sensoriais (opcional)
  - assignedTo: IDs de usuários designados (opcional)
- **Resposta**: Tarefa criada com ID

#### 16. Listar Tarefas
- **Endpoint**: GET /tasks
- **Descrição**: Retorna todas as tarefas do usuário
- **Parâmetros**: Nenhum
- **Resposta**: Lista de tarefas

#### 17. Obter Tarefa
- **Endpoint**: GET /tasks/:id
- **Descrição**: Retorna uma tarefa específica
- **Parâmetros**:
  - id: ID da tarefa
- **Resposta**: Detalhes da tarefa

#### 18. Atualizar Tarefa
- **Endpoint**: PATCH /tasks/:id
- **Descrição**: Atualiza uma tarefa existente
- **Parâmetros**:
  - id: ID da tarefa
  - title: Título da tarefa (opcional)
  - description: Descrição da tarefa (opcional)
  - dueDate: Data de vencimento (opcional)
  - priority: Prioridade (opcional)
  - sensoryTags: Tags sensoriais (opcional)
  - assignedTo: IDs de usuários designados (opcional)
  - completed: Status de conclusão (opcional)
- **Resposta**: Tarefa atualizada

#### 19. Deletar Tarefa
- **Endpoint**: DELETE /tasks/:id
- **Descrição**: Remove uma tarefa
- **Parâmetros**:
  - id: ID da tarefa
- **Resposta**: Confirmação de remoção

### Inteligência Artificial

#### 20. Gerar Resposta com IA
- **Endpoint**: POST /ai/generate-response
- **Descrição**: Gera uma resposta usando IA com base no prompt do usuário
- **Parâmetros**:
  - prompt: Texto de entrada do usuário
  - context: Contexto da conversa (opcional)
- **Resposta**: Resposta gerada pela IA

#### 21. Sumarizar Tarefas
- **Endpoint**: POST /ai/summarize-tasks
- **Descrição**: Usa IA para criar um resumo das tarefas do usuário
- **Parâmetros**:
  - tasks: Lista de tarefas a serem resumidas
- **Resposta**: Resumo gerado pela IA

#### 22. Salvar Feedback sobre IA
- **Endpoint**: POST /ai/feedback
- **Descrição**: Registra feedback do usuário sobre uma resposta da IA
- **Parâmetros**:
  - feedback: Texto do feedback
  - promptId: ID do prompt original
- **Resposta**: Confirmação de feedback salvo

#### 23. Listar Histórico de IA
- **Endpoint**: GET /ai/history
- **Descrição**: Retorna o histórico de interações do usuário com a IA
- **Parâmetros**: Nenhum
- **Resposta**: Lista de interações anteriores

### Gestão de Medicação

#### 24. Criar Medicação
- **Endpoint**: POST /medications
- **Descrição**: Registra uma nova medicação
- **Parâmetros**:
  - name: Nome da medicação
  - dosage: Dosagem
  - times: Horários para tomar
  - frequency: Frequência (diária, semanal, etc.)
- **Resposta**: Medicação criada com ID

#### 25. Atualizar Medicação
- **Endpoint**: PATCH /medications/:id
- **Descrição**: Atualiza informações de uma medicação
- **Parâmetros**:
  - id: ID da medicação
  - name: Nome da medicação (opcional)
  - dosage: Dosagem (opcional)
  - times: Horários para tomar (opcional)
  - frequency: Frequência (opcional)
- **Resposta**: Medicação atualizada

#### 26. Deletar Medicação
- **Endpoint**: DELETE /medications/:id
- **Descrição**: Remove uma medicação
- **Parâmetros**:
  - id: ID da medicação
- **Resposta**: Confirmação de remoção

### Integração com Agenda

#### 27. Criar Evento
- **Endpoint**: POST /calendar/events
- **Descrição**: Cria um novo evento na agenda
- **Parâmetros**:
  - title: Título do evento
  - date: Data do evento
  - time: Horário do evento
  - location: Local do evento (opcional)
- **Resposta**: Evento criado com ID

#### 28. Listar Eventos
- **Endpoint**: GET /calendar/events
- **Descrição**: Retorna todos os eventos do usuário
- **Parâmetros**: Nenhum
- **Resposta**: Lista de eventos

#### 29. Atualizar Evento
- **Endpoint**: PATCH /calendar/events/:id
- **Descrição**: Atualiza um evento existente
- **Parâmetros**:
  - id: ID do evento
  - title: Título do evento (opcional)
  - date: Data do evento (opcional)
  - time: Horário do evento (opcional)
  - location: Local do evento (opcional)
- **Resposta**: Evento atualizado

#### 30. Deletar Evento
- **Endpoint**: DELETE /calendar/events/:id
- **Descrição**: Remove um evento
- **Parâmetros**:
  - id: ID do evento
- **Resposta**: Confirmação de remoção

#### 31. Iniciar Autenticação Google
- **Endpoint**: GET /calendar/google/auth
- **Descrição**: Inicia o processo de autenticação OAuth com Google
- **Parâmetros**: Nenhum
- **Resposta**: Redirecionamento para página de login do Google

#### 32. Callback de Autenticação Google
- **Endpoint**: GET /calendar/google/callback
- **Descrição**: Finaliza o processo de autenticação OAuth
- **Parâmetros**:
  - code: Código de autorização fornecido pelo Google
- **Resposta**: Tokens de acesso e atualização

#### 33. Sincronizar Evento com Google
- **Endpoint**: POST /calendar/sync
- **Descrição**: Sincroniza um evento local com o Google Calendar
- **Parâmetros**:
  - eventId: ID do evento local
  - googleToken: Token de acesso do Google
- **Resposta**: Confirmação de sincronização

### Monitoramento de Saúde da API

#### 34. Verificar Saúde da API
- **Endpoint**: GET /health
- **Descrição**: Verifica se a API está funcionando corretamente
- **Parâmetros**: Nenhum
- **Resposta**: Status de saúde da API

## Cenários de Teste

### TC001 - Cadastro de Novo Usuário
- **Endpoint**: POST /auth/register
- **Descrição**: Criar novo usuário e retornar JWT
- **Dados de Teste**:
  ```json
  {
    "auth": {
      "local": {
        "email": "teste@exemplo.com",
        "password": "senha123"
      }
    },
    "profile": {
      "name": "Usuário Teste",
      "age": 30
    },
    "system": {
      "lang": "pt"
    }
  }
  ```
- **Resultado Esperado**: Status 201, token JWT retornado

### TC002 - Login com Credenciais Válidas
- **Endpoint**: POST /auth/login
- **Descrição**: Validar e autenticar usuário
- **Dados de Teste**:
  ```json
  {
    "email": "teste@exemplo.com",
    "password": "senha123"
  }
  ```
- **Resultado Esperado**: Status 200, token JWT retornado

### TC003 - Login com Senha Inválida
- **Endpoint**: POST /auth/login
- **Descrição**: Rejeitar login com senha errada
- **Dados de Teste**:
  ```json
  {
    "email": "teste@exemplo.com",
    "password": "senha_errada"
  }
  ```
- **Resultado Esperado**: Status 401, mensagem de erro

### TC004 - Criar Entrada Diária
- **Endpoint**: POST /dailyentries
- **Descrição**: Registrar emoções/relato do dia
- **Dados de Teste**:
  ```json
  {
    "text": "Hoje foi um dia produtivo",
    "date": "2025-04-23",
    "mood": 4
  }
  ```
- **Resultado Esperado**: Status 201, entrada criada

### TC005 - Buscar Entradas
- **Endpoint**: GET /dailyentries
- **Descrição**: Listar registros do usuário
- **Dados de Teste**: N/A
- **Resultado Esperado**: Status 200, lista de entradas

### TC006 - Deletar Entrada
- **Endpoint**: DELETE /dailyentries/:id
- **Descrição**: Remover entrada específica
- **Dados de Teste**: ID válido de entrada existente
- **Resultado Esperado**: Status 200, confirmação de remoção

### TC007 - Criar Tarefa
- **Endpoint**: POST /tasks
- **Descrição**: Registrar uma nova tarefa
- **Dados de Teste**:
  ```json
  {
    "title": "Completar relatório",
    "description": "Finalizar relatório mensal",
    "dueDate": "2025-04-30",
    "priority": 3
  }
  ```
- **Resultado Esperado**: Status 201, tarefa criada

### TC008 - Listar Tarefas
- **Endpoint**: GET /tasks
- **Descrição**: Listar tarefas do usuário
- **Dados de Teste**: N/A
- **Resultado Esperado**: Status 200, lista de tarefas

### TC009 - Gerar Resposta com IA
- **Endpoint**: POST /ai/generate-response
- **Descrição**: Obter resposta da IA
- **Dados de Teste**:
  ```json
  {
    "prompt": "Como posso melhorar meu foco?",
    "context": "TDAH"
  }
  ```
- **Resultado Esperado**: Status 200, resposta da IA

### TC010 - Criar Medicação
- **Endpoint**: POST /medications
- **Descrição**: Registrar nova medicação
- **Dados de Teste**:
  ```json
  {
    "name": "Ritalina",
    "dosage": "10mg",
    "times": ["08:00", "14:00"],
    "frequency": "daily"
  }
  ```
- **Resultado Esperado**: Status 201, medicação criada

### TC011 - Criar Evento na Agenda
- **Endpoint**: POST /calendar/events
- **Descrição**: Adicionar evento à agenda
- **Dados de Teste**:
  ```json
  {
    "title": "Consulta médica",
    "date": "2025-05-15",
    "time": "14:30",
    "location": "Clínica Central"
  }
  ```
- **Resultado Esperado**: Status 201, evento criado

### TC012 - Token Inválido
- **Endpoint**: GET /tasks
- **Descrição**: Rejeitar requisição sem autenticação
- **Dados de Teste**: Token inválido ou ausente
- **Resultado Esperado**: Status 401, mensagem de erro

## Modelos de Dados

### User
```json
{
  "type": "object",
  "properties": {
    "_id": {"type": "string"},
    "name": {"type": "string"},
    "email": {"type": "string"},
    "password": {"type": "string"}
  },
  "required": ["name", "email", "password"]
}
```

### UserRegistration
```json
{
  "type": "object",
  "properties": {
    "auth": {
      "type": "object",
      "properties": {
        "local": {
          "type": "object",
          "properties": {
            "email": {"type": "string"},
            "password": {"type": "string"}
          },
          "required": ["email", "password"]
        }
      }
    },
    "profile": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
      },
      "required": ["name", "age"]
    },
    "neuroProfile": {
      "type": "object",
      "properties": {
        "type": {"type": "string"},
        "diagnoses": {
          "type": "array",
          "items": {"type": "string"}
        },
        "symptoms": {
          "type": "array",
          "items": {"type": "string"}
        },
        "medicationSchedule": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "dosage": {"type": "string"},
              "times": {
                "type": "array",
                "items": {"type": "string"}
              }
            }
          }
        }
      }
    },
    "preferences": {"type": "object"},
    "system": {
      "type": "object",
      "properties": {
        "lang": {"type": "string", "example": "pt"}
      }
    }
  }
}
```

### Task
```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "description": {"type": "string"},
    "dueDate": {"type": "string", "format": "date"},
    "priority": {"type": "number"},
    "sensoryTags": {
      "type": "array",
      "items": {"type": "string"}
    },
    "assignedTo": {
      "type": "array",
      "items": {"type": "string"}
    },
    "completed": {"type": "boolean"}
  },
  "required": ["title"]
}
```

### DailyEntry
```json
{
  "type": "object",
  "properties": {
    "text": {"type": "string"},
    "date": {"type": "string", "format": "date"},
    "mood": {"type": "number"}
  },
  "required": ["mood", "date"]
}
```

### Medication
```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "dosage": {"type": "string"},
    "times": {
      "type": "array",
      "items": {"type": "string"}
    },
    "frequency": {"type": "string"}
  },
  "required": ["name", "dosage"]
}
```

### CalendarEvent
```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "date": {"type": "string"},
    "time": {"type": "string"},
    "location": {"type": "string"}
  },
  "required": ["title", "date"]
}
```

## Diagramas de Fluxo

Os diagramas de fluxo para cada funcionalidade principal estão disponíveis na documentação completa. Eles ilustram os processos de:

1. Cadastro e Perfil do Usuário
2. Entrada Diária (Journaling)
3. Gerenciamento de Tarefas
4. Gestão de Medicação
5. Integração com Agenda
6. Chat IA Personalizado
7. Análises e Relatórios
8. Configurações de Segurança
9. Preferências Avançadas
10. Resumo Final e Home
