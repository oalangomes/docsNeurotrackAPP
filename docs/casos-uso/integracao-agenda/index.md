# Integração com Agenda

O módulo de Integração com Agenda do NeurotrackApp permite aos usuários gerenciar seus compromissos e eventos, com sincronização bidirecional com o Google Calendar, ajudando pessoas neurodivergentes a manter uma rotina organizada e previsível.

## Diagrama de Fluxo

![Integração com Agenda](/assets/images/integracao_agenda_consolidado.png)

## Principais Funcionalidades

### Gerenciamento de Eventos
- **Criação de novo evento**: Interface simplificada para adicionar compromissos
- **Definição de detalhes**: Título, data, horário, local, categoria
- **Configuração de lembretes**: Alertas personalizados para eventos
- **Definição de recorrência**: Configuração de eventos periódicos
- **Visualização do calendário**: Diferentes visualizações (dia, semana, mês)
- **Filtragem de eventos**: Organização por categoria ou data

### Integração com Google Calendar
- **Autenticação e autorização**: Conexão segura com a conta Google
- **Sincronização bidirecional**: Eventos atualizados em ambas as plataformas
- **Importação de eventos**: Transferência de eventos do Google Calendar
- **Exportação de eventos**: Envio de eventos do NeurotrackApp para o Google Calendar
- **Resolução de conflitos**: Tratamento de eventos sobrepostos ou duplicados

### Gerenciamento
- **Visualização de detalhes**: Acesso a informações completas de cada evento
- **Edição e exclusão**: Possibilidade de modificar ou remover eventos
- **Marcação como concluído**: Registro de participação em eventos
- **Notificações adaptativas**: Lembretes ajustados ao perfil neurodivergente

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /agenda/events | Criação de novo evento |
| GET | /agenda/events | Listagem de eventos |
| GET | /agenda/events/{id} | Obtenção de detalhes de um evento específico |
| PUT | /agenda/events/{id} | Atualização de um evento existente |
| DELETE | /agenda/events/{id} | Exclusão de um evento |
| POST | /agenda/google/auth | Autenticação com Google Calendar |
| GET | /agenda/google/sync | Sincronização com Google Calendar |
| POST | /agenda/events/{id}/complete | Marcação de evento como concluído |

## Cenários de Uso

### Criação de Novo Evento
1. Usuário acessa a seção de Agenda
2. Seleciona a opção para criar novo evento
3. Insere título, data e horário do compromisso
4. Adiciona local (físico ou virtual)
5. Seleciona categoria do evento (trabalho, pessoal, saúde, etc.)
6. Configura lembretes personalizados
7. Define recorrência, se aplicável
8. Salva o evento e recebe confirmação

### Sincronização com Google Calendar
1. Usuário acessa configurações da Agenda
2. Seleciona opção de conectar com Google Calendar
3. Autoriza acesso à sua conta Google
4. Escolhe direção da sincronização (importar, exportar ou ambos)
5. Sistema realiza sincronização inicial
6. Eventos são atualizados em ambas as plataformas
7. Usuário recebe confirmação de sincronização concluída

### Gerenciamento de Rotina para Usuário com TEA
1. Usuário com perfil TEA visualiza agenda semanal
2. Sistema apresenta eventos com códigos de cores consistentes
3. Lembretes são configurados com maior antecedência
4. Alterações na agenda são destacadas visualmente
5. Eventos incluem informações detalhadas sobre o que esperar
6. Transições entre atividades são marcadas com alertas específicos
