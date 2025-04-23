# Entradas Diárias

O módulo de Entradas Diárias do NeurotrackApp permite aos usuários registrar seu humor, atividades e observações diárias, criando um histórico que pode ser analisado para identificar padrões e tendências.

## Diagrama de Fluxo

![Entradas Diárias](../assets/images/entradas_diarias_consolidado.png)

## Principais Funcionalidades

### Registro de Entradas
- **Criação de nova entrada diária**: Interface intuitiva para registro rápido
- **Registro de humor**: Escala visual de 1-5 para facilitar a identificação do estado emocional
- **Adição de texto**: Campo para descrição detalhada do dia
- **Uso de tags**: Categorização das entradas para facilitar análises futuras
- **Anexo de mídia**: Possibilidade de adicionar fotos ou áudios às entradas

### Visualização e Gerenciamento
- **Visualização de entradas anteriores**: Histórico organizado cronologicamente
- **Filtragem por período**: Seleção de intervalos específicos para análise
- **Visualização de detalhes**: Acesso a informações completas de cada entrada
- **Edição e exclusão**: Possibilidade de modificar ou remover entradas existentes

### Análise e Relatórios
- **Análise de padrões com IA**: Identificação de correlações entre humor e atividades
- **Geração de relatórios de humor**: Visualização gráfica da evolução do humor ao longo do tempo
- **Insights personalizados**: Recomendações baseadas nos padrões identificados

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /daily-entries | Criação de nova entrada diária |
| GET | /daily-entries | Listagem de entradas diárias |
| GET | /daily-entries/{id} | Obtenção de detalhes de uma entrada específica |
| PUT | /daily-entries/{id} | Atualização de uma entrada existente |

## Cenários de Uso

### Registro de Nova Entrada Diária
1. Usuário acessa a seção de Entradas Diárias
2. Seleciona a opção para criar nova entrada
3. Registra seu humor na escala visual
4. Adiciona descrição textual sobre seu dia
5. Seleciona tags relevantes (ex: trabalho, estudo, lazer)
6. Opcionalmente anexa mídia
7. Salva a entrada e recebe confirmação

### Visualização de Histórico de Humor
1. Usuário acessa a seção de Entradas Diárias
2. Seleciona a opção de visualizar relatórios
3. Escolhe o tipo de relatório (ex: gráfico de humor)
4. Define o período desejado para análise
5. Visualiza o gráfico de evolução do humor
6. Pode exportar ou compartilhar o relatório

### Análise de Padrões com IA
1. Usuário acessa a seção de Entradas Diárias
2. Seleciona a opção de análise de padrões
3. A IA processa as entradas do período selecionado
4. Sistema apresenta correlações identificadas (ex: humor melhor em dias com exercício físico)
5. Usuário recebe recomendações personalizadas baseadas na análise
