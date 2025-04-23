# Análises e Relatórios

O módulo de Análises e Relatórios do NeurotrackApp oferece visualizações detalhadas e insights sobre os dados coletados em todos os outros módulos, permitindo que usuários neurodivergentes identifiquem padrões e tendências em seu comportamento, humor, produtividade e saúde.

## Diagrama de Fluxo

![Análises e Relatórios](../assets/images/analises_relatorios_consolidado.png)

## Principais Funcionalidades

### Dashboard Principal
- **Resumo de humor**: Visualização da evolução do estado emocional
- **Progresso de tarefas**: Métricas de conclusão e produtividade
- **Aderência à medicação**: Taxa de cumprimento do tratamento
- **Calendário de eventos**: Visão geral de compromissos
- **Insights da IA**: Observações personalizadas baseadas nos dados

### Relatórios Específicos
- **Relatórios de humor**: Análise detalhada das entradas diárias
- **Relatórios de tarefas**: Métricas de produtividade e conclusão
- **Relatórios de medicação**: Histórico de aderência ao tratamento
- **Relatórios de agenda**: Análise de compromissos e tempo

### Análises Personalizadas
- **Seleção de período**: Definição do intervalo para análise
- **Escolha de métricas**: Seleção dos dados a serem analisados
- **Tipos de visualização**: Gráficos, tabelas, mapas de calor
- **Correlações entre dados**: Identificação de relações entre diferentes métricas

### Exportação e Compartilhamento
- **Formatos de exportação**: PDF, CSV, imagens
- **Compartilhamento por e-mail**: Envio direto para contatos
- **Compartilhamento com profissionais**: Envio para médicos e terapeutas
- **Histórico de relatórios**: Acesso a análises anteriores

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /analytics/dashboard | Obtenção de dados para o dashboard principal |
| GET | /analytics/mood | Geração de relatório de humor |
| GET | /analytics/tasks | Geração de relatório de tarefas |
| GET | /analytics/medication | Geração de relatório de medicação |
| GET | /analytics/agenda | Geração de relatório de agenda |
| POST | /analytics/custom | Criação de análise personalizada |
| POST | /analytics/export | Exportação de relatório em formato específico |
| POST | /analytics/share | Compartilhamento de relatório |

## Cenários de Uso

### Visualização do Dashboard Principal
1. Usuário acessa a seção de Análises e Relatórios
2. Sistema carrega o dashboard principal com resumo de todos os módulos
3. Usuário visualiza gráficos de humor, tarefas, medicação e agenda
4. Insights da IA destacam padrões importantes identificados
5. Usuário pode interagir com os gráficos para obter mais detalhes
6. Sistema oferece opções para aprofundar a análise em áreas específicas

### Geração de Relatório Personalizado
1. Usuário acessa a seção de Análises Personalizadas
2. Seleciona o período desejado para análise
3. Escolhe as métricas a serem incluídas no relatório
4. Define o tipo de visualização preferido
5. Sistema processa os dados e gera o relatório
6. Usuário pode ajustar parâmetros para refinar a análise
7. Visualiza o relatório final e pode exportá-lo ou compartilhá-lo

### Compartilhamento com Profissional de Saúde
1. Usuário gera um relatório específico (ex: humor e medicação)
2. Seleciona a opção de compartilhar
3. Escolhe o formato de exportação (geralmente PDF)
4. Adiciona e-mail do profissional de saúde
5. Opcionalmente inclui uma mensagem personalizada
6. Sistema envia o relatório e notifica o usuário
7. O relatório inclui contexto e explicações para facilitar a interpretação
