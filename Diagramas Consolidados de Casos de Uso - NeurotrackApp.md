# Diagramas Consolidados de Casos de Uso - NeurotrackApp

Este documento apresenta os diagramas consolidados de casos de uso para o NeurotrackApp, uma aplicação desenvolvida para auxiliar pessoas neurodivergentes no gerenciamento de suas atividades diárias, medicações, compromissos e bem-estar.

## Índice

1. [Resumo e Home](#resumo-e-home)
2. [Autenticação e Perfil](#autenticação-e-perfil)
3. [Entradas Diárias](#entradas-diárias)
4. [Gerenciamento de Tarefas](#gerenciamento-de-tarefas)
5. [Inteligência Artificial](#inteligência-artificial)
6. [Gestão de Medicação](#gestão-de-medicação)
7. [Integração com Agenda](#integração-com-agenda)
8. [Análises e Relatórios](#análises-e-relatórios)
9. [Configurações de Segurança](#configurações-de-segurança)
10. [Preferências Avançadas](#preferências-avançadas)

## Resumo e Home

O diagrama abaixo representa a tela inicial (Home) do NeurotrackApp, mostrando o fluxo desde o acesso ao aplicativo até a navegação para os diferentes módulos.

![Resumo e Home](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L3Jlc3Vtb19ob21lX2NvbnNvbGlkYWRv.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjM1Z0YjE5b2IyMWxYMk52Ym5OdmJHbGtZV1J2LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=vUV6KWzj24f39637V8LnqDhlZWwxmDEGh0q0DWQP10aZFYQ7xMYLmHS6kfDBr46mwhAd1cX5RTBD6a2gxuH0FtGZmRmMexA2SLPkI8ioX6MNvG3kicq5PQX2WV8nSA8N2YRi1g~aGAQ~GxwgZhi2anPwcluDv7pQynesZZADRchUM4vdt9XaTlHZS5qPBbfM41vh-A-AY3E2oKReHZR-U3yhR8I-yz0nNmMA05arYGfZw0f0WeNmgoSFI4302XRcNFoWM0lgNxFCI4u~cqWSEUB6MR1OL63HgXXNqiDX9gfx4YZLKfylQR6UkYgUeIz~nZOrbOTa-~j4HByKWPdRaQ__)

**Principais funcionalidades:**
- Dashboard de resumo com widgets personalizáveis
- Menu de navegação para todos os módulos
- Centro de notificações
- Acesso rápido aos módulos mais utilizados
- Componentes do dashboard: resumo de humor, próximas tarefas, lembretes de medicação, próximos eventos e insights diários
- Personalização da Home: reordenar widgets, ocultar/mostrar widgets, ajustar tamanho e definir layout padrão

## Autenticação e Perfil

O diagrama abaixo representa o fluxo de autenticação e gerenciamento de perfil do usuário no NeurotrackApp.

![Autenticação e Perfil](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2F1dGVudGljYWNhb19wZXJmaWxfY29uc29saWRhZG8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyRjFkR1Z1ZEdsallXTmhiMTl3WlhKbWFXeGZZMjl1YzI5c2FXUmhaRzgucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=jdAd1lIpw-C4EY7c9WtNGYpCBkhCK0-ipiQUa1uPCKV2tfHo8nCnK2zXLQ0WFHOxQ9GOPyXVtmKSwZ~TVPrONMV~sIM~~T5iseBTSgufDjc4RISx9h65~fWH0tK5pCPyor9cqCgB4pWbCNPbEcCq-2Sisq3~Mvb1Z8MDA582OPVLP5WU~d4l46VVy~frXXfATGfm7DQ~B32ztuXL3fulu2HeLubI4OcEYe6bx5z6zcZfCoFjBjgXU9NZZlviDVfDOkeTfVKIeK2PvDGKPGj4urPPzj0gnxMft7QcAFsCkMV35s7rbQ0MSXF~8jzCk73m9H4VXbUwdQWULzfsyTeSyA__)

**Principais funcionalidades:**
- Opções de login: e-mail/senha, Google, biometria
- Cadastro de novo usuário
- Configuração de perfil neurodivergente
- Definição de preferências de interação
- Gerenciamento de perfil: visualização, edição de dados, atualização de senha, edição de perfil neurodivergente, gerenciamento de preferências

## Entradas Diárias

O diagrama abaixo representa o fluxo de criação e gerenciamento de entradas diárias no NeurotrackApp.

![Entradas Diárias](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2VudHJhZGFzX2RpYXJpYXNfY29uc29saWRhZG8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyVnVkSEpoWkdGelgyUnBZWEpwWVhOZlkyOXVjMjlzYVdSaFpHOC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Q2eTxMHZ37OkETzEB5-zcYl8lEB~zXs~82HpYwOVfaTaSB6R8h--YV1Iwcm6YQXFyKiCeyWId0SpMJj2ULVqWwsxd2ivrRgW-6OLHH5N33vHdb2Zo~HMJClyAMyNSKi0PpEBiGnD7NM80YOeIlepbAQFe6Qo-tGHpeNCIpNjPVtdBpzTeyLmzeMK9zY~TfyGXGo6ZSigy2g1OnY5J6k5hipwiN1JDT0wL8cdFx1PiUTTg-yxvEH5E5Re4EaZNkcbbd2J1uu2SHmTtS03lO1Ov~~L1CmSfRCG2PySVpfZd96UXWI1igGei4U0VH~3MiI8qrfQNoCzt8L3AsBS5wqzDg__)

**Principais funcionalidades:**
- Criação de nova entrada diária
- Visualização de entradas anteriores
- Filtragem de entradas por período
- Registro de humor (escala 1-5)
- Adição de texto, tags e mídia
- Visualização de detalhes, edição e exclusão de entradas
- Análise de padrões com IA
- Geração de relatórios de humor

## Gerenciamento de Tarefas

O diagrama abaixo representa o fluxo de gerenciamento de tarefas no NeurotrackApp.

![Gerenciamento de Tarefas](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2dlcmVuY2lhbWVudG9fdGFyZWZhc19jb25zb2xpZGFkbw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZGxjbVZ1WTJsaGJXVnVkRzlmZEdGeVpXWmhjMTlqYjI1emIyeHBaR0ZrYncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ijV3An05gbUOZFi6kY02u-YcML7graZWCluVp9EeorAsDeS2WGoDvHkfFFQx4KVJO9aTlEcIVdXvD9aIXz~DxRLmVutId5HAwN20q45JUrAe-eZ5CNCzCKn6MYEgv48~BBsnqLsO~lLHSJfRcBqzSGPpdVyMWnqc590gCrFuIkgJ6SewJCoy8~Cpu5YC3N5BKt-Fy6O3SSxMUuqlmKt-rDh6C2eKyttBCNTtkW18~Hcnqw7eGwtVzFMZis6CBAvRQrw2JocWeCxYKJKZVs-HENA9veXHQZRjrhXGKGlLBM8ZJPq4mFPq7t8CLFunm2z028to7e4esj2afUSath8m-w__)

**Principais funcionalidades:**
- Criação de nova tarefa
- Visualização da lista de tarefas
- Filtragem de tarefas por status/prioridade
- Definição de título, descrição, prioridade, tags sensoriais, data de vencimento
- Adição de subtarefas
- Assistência de IA: sugestão de decomposição de tarefas complexas, recomendação de prioridades, estimativa de tempo
- Gerenciamento: visualização de detalhes, edição, marcação como concluída, exclusão, reordenação

## Inteligência Artificial

O diagrama abaixo representa o fluxo de interação com a inteligência artificial no NeurotrackApp.

![Inteligência Artificial](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2ludGVsaWdlbmNpYV9hcnRpZmljaWFsX2NvbnNvbGlkYWRv.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwybHVkR1ZzYVdkbGJtTnBZVjloY25ScFptbGphV0ZzWDJOdmJuTnZiR2xrWVdSdi5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=l90eimIJkpWfRNKIt9dFR6wOuDoo4z1SDM0rBsX4B7HLlK2AAhDqB8PuMLtrLdN25NA8txsVceZybWp7Z70-Cued2SBoTMeuovvBMp5~c9IhX0b3JbSHJMVWNm4K5qW7PmVMZnq82acI-ut~BcCsqRQnVGE-vJQMaM~R6ipfgL9ZWUO-C9sCKmD8A4hhhszDXub4mB~BnP4nyKghQCsrOfA9BY0i1tJ~Y2aCYDIZ7LQKnsrdZ~CySO4LhMtVIaAnu28U-7uiLIqKvv-Fo323bXSg9gwt7~jxuLLF9NEXMwRuUnHAyQ43TmoQxMfDGeitcQu1vkJsyPABFEwTyW45PA__)

**Principais funcionalidades:**
- Chat com IA
- Solicitação de análise de dados
- Visualização do histórico de interações
- Envio de prompts/perguntas e recebimento de respostas
- Fornecimento de contexto para a conversa
- Avaliação de respostas (feedback)
- Análise de dados: seleção de dados, escolha do tipo de análise (humor, tarefas, medicação)
- Personalização da IA: ajuste de estilo de comunicação, definição de preferências de interação, treinamento do modelo com feedback

## Gestão de Medicação

O diagrama abaixo representa o fluxo de gestão de medicação no NeurotrackApp.

![Gestão de Medicação](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2dlc3Rhb19tZWRpY2FjYW9fY29uc29saWRhZG8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZGxjM1JoYjE5dFpXUnBZMkZqWVc5ZlkyOXVjMjlzYVdSaFpHOC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=irXA9Bx32WHjFNF98gqIjOFxF5i1yIpjkSUvKlg9k-r7HOcr0ScZ6~p162Tqgjku8ecw7c1LAUvnJWVOdBu141Kx9rLcy7~WZyEJzem8kFYbZITxgFXa85nbwlY9aNqBmHr~31LDtqBEMtj~fcWzPZNNnHE6D9cp5N2XBzBH2ZG8hqO214mRVJ2DxWA2ZRXR2hyOUqA~OqSxpMwd6v-~ziVdmoKOLj9kD2zuXw93GjAHoucvqQsoDF~2lKCoOIW0RqvGBD8QC6YJMvlVJso4EOArDrCaVCwA5CzCaf~fuqEWGeHe8M5Un~fzgQ6HNuyRIXKf7lJl1r7aqJSrx6FKPQ__)

**Principais funcionalidades:**
- Adição de nova medicação
- Visualização da lista de medicações
- Visualização do histórico de aderência
- Definição de nome, dosagem, frequência, horários, duração e observações
- Configuração de lembretes
- Gerenciamento: visualização de detalhes, edição, exclusão, marcação como tomada
- Monitoramento e relatórios: verificação de taxa de aderência, geração e compartilhamento de relatórios

## Integração com Agenda

O diagrama abaixo representa o fluxo de integração com agenda no NeurotrackApp.

![Integração com Agenda](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746307_na1fn_L2hvbWUvdWJ1bnR1L2ludGVncmFjYW9fYWdlbmRhX2NvbnNvbGlkYWRv.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwybHVkR1ZuY21GallXOWZZV2RsYm1SaFgyTnZibk52Ykdsa1lXUnYucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=mOdLLEsqQ3yB7PJ71eJx1FRXkMD8kyziTJfW3o6CVW~iSBLwjlki1865q1BIIiC5oSONjBU9P9qB9gxcMEL9vx9oMAllhdfyCa6-Du9OkTaTciPaBxlK1vB66p4hQf-0Jit7l9GTw5GkWWV-Blzy7uxT0pQjdV~lBpmiurZSFw~-lE-PVDGxDiMlYvahocioaUjXQLxuZ8FVyzCaOYT7XxbRDwowvDA2y87jaCelrUz~HBw7HMzuE7t6c9qRhyiZ9SHqgW4QPrOqj09uH8qwfQSodY2~vNSBUVxtvBY0bY4jX0T3imfto3-KxfoGkOWwQIyO73yvx7pxsGJrKjmPJQ__)

**Principais funcionalidades:**
- Criação de novo evento
- Visualização do calendário
- Filtragem de eventos por categoria/data
- Definição de título, data, horário, local, categoria
- Configuração de lembretes e recorrência
- Gerenciamento: visualização de detalhes, edição, exclusão, marcação como concluído
- Integração com Google Calendar: autenticação, autorização de acesso, sincronização, importação e exportação de eventos

## Análises e Relatórios

O diagrama abaixo representa o fluxo de análises e relatórios no NeurotrackApp.

![Análises e Relatórios](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746308_na1fn_L2hvbWUvdWJ1bnR1L2FuYWxpc2VzX3JlbGF0b3Jpb3NfY29uc29saWRhZG8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyRnVZV3hwYzJWelgzSmxiR0YwYjNKcGIzTmZZMjl1YzI5c2FXUmhaRzgucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Q2wnBnyo4GNW0FFKwrGHh-oA57S7NMvQdSp2CE79czoZ9LVXaN7YYf~yCZHOPc1DKRCyJJE5oMP21-TsfdiLdf5mT6Gh2oS9R5X7CtWACI-qrkqu97c-DavEaXNw3gzkV-uAnm3FvgUgFS21~h~wTdEQbYhlmOCsR1VI96fRHjpMmKhCNjDVvAfz9J4DQNSp-8xloU-dTffCL2pQP7BeYF-XKi3Muwlll9X0~UxdhDAdt4PgFN9E4uUT5sf5q3D-6KyotkN399SKZJFKVuwxijvMC94HqRsjv9QibMzA4ET0UBW~tPl8B8RZ~Ztb8tE44Wiex9ATQODmawoG-yxBAA__)

**Principais funcionalidades:**
- Visualização do dashboard principal
- Acesso a relatórios específicos
- Criação de análises personalizadas
- Dashboard principal: resumo de humor, progresso de tarefas, aderência à medicação, calendário de eventos, insights da IA
- Relatórios específicos: humor, tarefas, medicação, agenda
- Análises personalizadas: seleção de período, métricas e tipo de visualização
- Exportação e compartilhamento: PDF, CSV, e-mail, profissional de saúde

## Configurações de Segurança

O diagrama abaixo representa o fluxo de configurações de segurança no NeurotrackApp.

![Configurações de Segurança](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746308_na1fn_L2hvbWUvdWJ1bnR1L2NvbmZpZ3VyYWNvZXNfc2VndXJhbmNhX2NvbnNvbGlkYWRv.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZibVpwWjNWeVlXTnZaWE5mYzJWbmRYSmhibU5oWDJOdmJuTnZiR2xrWVdSdi5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ntL6rS4dontrMnPwUoudGwAJMzpte5bWVBoeyn20Tg1jsZESLfNQWc8TJWpxPstTm6I6Jg02Q4WaoyvOpHLGL6IvHM~fir3uIkLxtNJbB2V0u~QzPHpvne0X~DZObPBw1yQPwBoWguAjzdlp2HPPk2IYgjwQOH3tbLry~x~s42-GB78yzLgt-6fbMlhKefY9jjXPj4zryNiX~sy5kO1cxZm0YPm8DJfWHKvguR~uthUbNYwWqw12lW6QSZotE~MVMQDm4~M~JgQHhpEl7dhhRCYGXH3a~KlmNSivVgWIkjTpPY7NwtF7UtRgMN~4zaYyZfAl751mmqVlhsZMvyvV8w__)

**Principais funcionalidades:**
- Gerenciamento de métodos de autenticação
- Configuração de opções de privacidade
- Gerenciamento de dados pessoais
- Autenticação: alteração de senha, configuração de biometria, ativação de 2FA, gerenciamento de sessões
- Privacidade: definição de visibilidade de dados, configuração de compartilhamento, gerenciamento de permissões, configuração de notificações
- Dados pessoais: visualização, exportação, exclusão, configuração de backup

## Preferências Avançadas

O diagrama abaixo representa o fluxo de preferências avançadas no NeurotrackApp.

![Preferências Avançadas](https://private-us-east-1.manuscdn.com/sessionFile/5KrJGMixfqGgdw7cYMnU2n/sandbox/jrpUa3TXWzEohQUxerJfww-images_1745412746308_na1fn_L2hvbWUvdWJ1bnR1L3ByZWZlcmVuY2lhc19hdmFuY2FkYXNfY29uc29saWRhZG8.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNUtySkdNaXhmcUdnZHc3Y1lNblUybi9zYW5kYm94L2pycFVhM1RYV3pFb2hRVXhlckpmd3ctaW1hZ2VzXzE3NDU0MTI3NDYzMDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzQnlaV1psY21WdVkybGhjMTloZG1GdVkyRmtZWE5mWTI5dWMyOXNhV1JoWkc4LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=E8mMrmK~EkUQGDgyhICKyMS8aIy5-GlLwH2cJcZXicHrdQ9Va-piD9M~BzcDCb7NP7pFA~Rjt5jS2m53DOrDhuv8rNmUuDRbrd4HCh8X7ZHzrB9g-R2dm~sD4dwRpS3rWof-7Ya25PsvwukPsNcETPoQ4YtJ413QopHsArl3zZZeo6pp5zNz7lgg146O4AQTZ15StsNJpSEulbZYYKlPBRgO1epFwm0upnTFmlHHX6E8ETZ1xG9vi3-iL0L~TJLrAafTVYzjshQ5DuhkxJX3oh3qWF79p1TwoKVwrT3~vw7L7fvTSDi0wK5GpuE-CbpU5H~94172rShebnP7O1sLgA__)

**Principais funcionalidades:**
- Personalização de interface
- Configuração de opções de acessibilidade
- Ajuste de perfil neurodivergente
- Interface: seleção de tema visual, ajuste de tamanho de fonte, configuração de layout, organização de módulos
- Acessibilidade: modo alto contraste, leitor de tela, navegação por voz, simplificação de interface
- Perfis neurodivergentes: TDAH, TEA, dislexia, personalizado
- Configurações específicas para TDAH: lembretes frequentes, temporizadores visuais, redução de distração
- Configurações específicas para TEA: previsibilidade, redução de estímulos, rotinas visuais
