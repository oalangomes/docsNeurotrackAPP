# Inteligência Artificial

O módulo de Inteligência Artificial do NeurotrackApp oferece assistência personalizada através de um chat com IA e análise de dados, adaptando-se às necessidades específicas de cada usuário neurodivergente.

## Diagrama de Fluxo

![Inteligência Artificial](../assets/images/inteligencia_artificial_consolidado.png)

## Principais Funcionalidades

### Chat com IA
- **Interação conversacional**: Interface de chat natural e acessível
- **Histórico de interações**: Registro de conversas anteriores para contexto
- **Envio de prompts/perguntas**: Possibilidade de fazer perguntas específicas
- **Fornecimento de contexto**: Capacidade de incluir informações adicionais para melhorar respostas
- **Avaliação de respostas**: Sistema de feedback para melhorar a qualidade das interações

### Análise de Dados
- **Seleção de dados**: Escolha dos tipos de dados a serem analisados
- **Tipos de análise**: Humor, tarefas, medicação, padrões de comportamento
- **Visualização de insights**: Apresentação clara das conclusões da análise
- **Recomendações personalizadas**: Sugestões baseadas nos padrões identificados

### Personalização da IA
- **Ajuste de estilo de comunicação**: Adaptação do tom e complexidade das respostas
- **Definição de preferências**: Configuração de como a IA deve interagir
- **Treinamento do modelo**: Aprendizado contínuo baseado no feedback do usuário
- **Adaptação ao perfil neurodivergente**: Ajustes específicos para TDAH, TEA, etc.

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /ai/chat | Envio de mensagem para o chat com IA |
| GET | /ai/chat/history | Obtenção do histórico de conversas |
| POST | /ai/analyze | Solicitação de análise de dados específicos |
| PUT | /ai/preferences | Atualização de preferências de interação com IA |

## Cenários de Uso

### Interação com Chat de IA
1. Usuário acessa a seção de Chat com IA
2. Visualiza histórico de conversas anteriores (se houver)
3. Digita uma pergunta ou solicitação
4. IA processa a entrada considerando o perfil do usuário
5. Sistema apresenta resposta adaptada às necessidades do usuário
6. Usuário pode fornecer feedback sobre a qualidade da resposta
7. IA ajusta seu modelo com base no feedback recebido

### Análise de Padrões de Humor
1. Usuário acessa a seção de Análise de Dados
2. Seleciona "Humor" como tipo de dados a analisar
3. Define o período desejado para análise
4. Sistema processa os dados das entradas diárias
5. IA identifica padrões e correlações
6. Apresenta visualização gráfica dos resultados
7. Oferece insights e recomendações personalizadas

### Personalização da IA para Usuário com TEA
1. Usuário com perfil TEA acessa configurações da IA
2. Ajusta preferências para comunicação mais direta e literal
3. Configura redução de estímulos visuais nas respostas
4. Define preferência por estrutura previsível nas interações
5. Sistema salva as configurações e adapta todas as interações futuras
6. IA passa a fornecer respostas mais estruturadas e previsíveis
