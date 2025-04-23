# Gerenciamento de Tarefas

O módulo de Gerenciamento de Tarefas do NeurotrackApp foi desenvolvido especialmente para auxiliar pessoas neurodivergentes a organizar suas atividades, dividindo-as em etapas menores e mais gerenciáveis, com assistência de IA para priorização e estimativa de tempo.

## Diagrama de Fluxo

![Gerenciamento de Tarefas](../assets/images/gerenciamento_tarefas_consolidado.png)

## Principais Funcionalidades

### Criação e Organização
- **Criação de nova tarefa**: Interface simplificada para adicionar tarefas rapidamente
- **Definição de detalhes**: Título, descrição, prioridade, data de vencimento
- **Tags sensoriais**: Identificação de estímulos associados à tarefa (visual, auditivo, etc.)
- **Adição de subtarefas**: Decomposição de tarefas complexas em etapas menores
- **Filtragem por status/prioridade**: Organização visual das tarefas pendentes

### Assistência de IA
- **Sugestão de decomposição**: IA auxilia na divisão de tarefas complexas
- **Recomendação de prioridades**: Sugestões baseadas em urgência e importância
- **Estimativa de tempo**: Previsão de tempo necessário para conclusão
- **Adaptação ao perfil**: Recomendações personalizadas conforme perfil neurodivergente

### Gerenciamento
- **Visualização de detalhes**: Acesso a informações completas de cada tarefa
- **Edição e exclusão**: Possibilidade de modificar ou remover tarefas existentes
- **Marcação como concluída**: Registro de progresso e conclusão
- **Reordenação**: Ajuste manual da ordem de prioridade das tarefas

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /tasks | Criação de nova tarefa |
| GET | /tasks | Listagem de tarefas |
| GET | /tasks/{id} | Obtenção de detalhes de uma tarefa específica |
| PUT | /tasks/{id} | Atualização de uma tarefa existente |
| DELETE | /tasks/{id} | Exclusão de uma tarefa |

## Cenários de Uso

### Criação de Nova Tarefa com Assistência de IA
1. Usuário acessa a seção de Gerenciamento de Tarefas
2. Seleciona a opção para criar nova tarefa
3. Insere título e descrição da tarefa
4. Solicita assistência da IA para decomposição
5. IA sugere divisão em subtarefas menores
6. Usuário ajusta as sugestões conforme necessário
7. Define prioridade e data de vencimento
8. Salva a tarefa e recebe confirmação

### Gerenciamento de Lista de Tarefas
1. Usuário acessa a seção de Gerenciamento de Tarefas
2. Visualiza lista de tarefas pendentes
3. Filtra por prioridade ou data de vencimento
4. Reordena tarefas conforme necessidade
5. Marca tarefas concluídas
6. Sistema atualiza progresso geral

### Adaptação para Perfil TDAH
1. Usuário com perfil TDAH acessa suas tarefas
2. Sistema apresenta interface com menos distrações
3. Tarefas são apresentadas com temporizadores visuais
4. Lembretes mais frequentes são configurados automaticamente
5. IA sugere quebrar tarefas em etapas ainda menores
6. Sistema oferece recompensas visuais ao completar tarefas
