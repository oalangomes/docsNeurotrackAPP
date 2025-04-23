# Resumo e Home

O módulo de Resumo e Home do NeurotrackApp serve como ponto central de acesso a todas as funcionalidades do aplicativo, oferecendo uma visão consolidada das informações mais relevantes para o usuário neurodivergente em um único local.

## Diagrama de Fluxo

![Resumo e Home](../assets/images/resumo_home_consolidado.png)

## Principais Funcionalidades

### Dashboard Personalizado
- **Widgets personalizáveis**: Componentes que podem ser reorganizados conforme preferência
- **Menu de navegação**: Acesso rápido a todos os módulos do aplicativo
- **Centro de notificações**: Alertas e lembretes consolidados
- **Acesso rápido**: Atalhos para as funcionalidades mais utilizadas
- **Visualização adaptativa**: Layout que se ajusta ao perfil neurodivergente do usuário

### Componentes do Dashboard
- **Resumo de humor**: Visualização do estado emocional recente
- **Próximas tarefas**: Lista das atividades pendentes mais urgentes
- **Lembretes de medicação**: Próximas medicações a serem tomadas
- **Próximos eventos**: Compromissos agendados para o período
- **Insights diários**: Recomendações personalizadas da IA

### Personalização da Home
- **Reordenar widgets**: Ajuste da posição dos componentes
- **Ocultar/mostrar widgets**: Controle sobre quais informações são exibidas
- **Ajustar tamanho**: Configuração do espaço ocupado por cada componente
- **Definir layout padrão**: Salvar configuração preferida
- **Temas visuais**: Adaptação da aparência conforme necessidades sensoriais

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /dashboard | Obtenção dos dados para o dashboard principal |
| GET | /dashboard/widgets | Listagem de widgets disponíveis |
| PUT | /users/dashboard/layout | Atualização do layout do dashboard |
| GET | /notifications | Obtenção de notificações pendentes |
| PUT | /users/quick-access | Configuração de atalhos de acesso rápido |

## Cenários de Uso

### Personalização Inicial do Dashboard
1. Usuário acessa o aplicativo pela primeira vez após configuração de perfil
2. Sistema apresenta layout padrão baseado no perfil neurodivergente
3. Usuário seleciona opção de personalizar dashboard
4. Escolhe quais widgets deseja exibir na tela inicial
5. Reorganiza os componentes conforme sua preferência
6. Ajusta o tamanho de cada widget
7. Salva o layout personalizado
8. Sistema aplica as configurações e exibe o novo dashboard

### Uso Diário da Home
1. Usuário abre o aplicativo
2. Visualiza resumo de seu humor recente
3. Verifica próximas tarefas pendentes
4. Recebe lembrete de medicações a serem tomadas
5. Consulta próximos compromissos na agenda
6. Acessa notificações pendentes
7. Navega para outros módulos através do menu principal

### Adaptação para Usuário com TDAH
1. Usuário com perfil TDAH acessa a Home
2. Sistema apresenta interface com menos distrações
3. Tarefas urgentes são destacadas visualmente
4. Lembretes de medicação incluem temporizadores visuais
5. Insights da IA oferecem dicas de foco e organização
6. Layout prioriza informações essenciais e minimiza elementos decorativos
