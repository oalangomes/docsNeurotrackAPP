# Gestão de Medicação

O módulo de Gestão de Medicação do NeurotrackApp permite aos usuários gerenciar seus medicamentos, configurar lembretes e monitorar a aderência ao tratamento, especialmente importante para pessoas neurodivergentes que podem ter dificuldades com rotinas e memória.

## Diagrama de Fluxo

![Gestão de Medicação](/assets/images/gestao_medicacao_consolidado.png)

## Principais Funcionalidades

### Cadastro e Gerenciamento
- **Adição de nova medicação**: Interface intuitiva para registro de medicamentos
- **Definição de detalhes**: Nome, dosagem, frequência, horários, duração e observações
- **Configuração de lembretes**: Alertas personalizados para horários de medicação
- **Visualização da lista de medicações**: Organização clara dos medicamentos cadastrados
- **Gerenciamento**: Visualização de detalhes, edição e exclusão de medicamentos

### Monitoramento
- **Marcação como tomada**: Registro de medicações administradas
- **Visualização do histórico de aderência**: Acompanhamento do cumprimento do tratamento
- **Verificação de taxa de aderência**: Estatísticas sobre o uso correto das medicações
- **Alertas de estoque baixo**: Notificações quando medicamentos estão acabando

### Relatórios
- **Geração de relatórios**: Compilação de dados sobre uso de medicamentos
- **Compartilhamento com profissionais**: Envio de informações para médicos e cuidadores
- **Análise de padrões**: Correlação entre uso de medicação e outros dados (humor, produtividade)

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /medications | Cadastro de nova medicação |
| GET | /medications | Listagem de medicações |
| GET | /medications/{id} | Obtenção de detalhes de uma medicação específica |
| PUT | /medications/{id} | Atualização de uma medicação existente |
| DELETE | /medications/{id} | Exclusão de uma medicação |
| POST | /medications/{id}/taken | Marcação de medicação como tomada |
| GET | /medications/adherence | Obtenção de relatório de aderência |

## Cenários de Uso

### Cadastro de Nova Medicação
1. Usuário acessa a seção de Gestão de Medicação
2. Seleciona a opção para adicionar nova medicação
3. Insere nome, dosagem e forma de administração
4. Define frequência (diária, semanal, etc.) e horários específicos
5. Configura duração do tratamento (se aplicável)
6. Adiciona observações importantes (ex: tomar com alimentos)
7. Configura lembretes personalizados
8. Salva a medicação e recebe confirmação

### Monitoramento de Aderência
1. Usuário recebe notificação no horário programado
2. Marca a medicação como tomada após administração
3. Sistema registra data e hora da administração
4. Usuário pode visualizar histórico de aderência
5. Sistema calcula taxa de aderência ao tratamento
6. Apresenta estatísticas e tendências de uso

### Compartilhamento com Profissional de Saúde
1. Usuário acessa a seção de relatórios de medicação
2. Seleciona período desejado para o relatório
3. Sistema gera relatório detalhado de uso de medicamentos
4. Usuário escolhe opção de compartilhar
5. Seleciona método de compartilhamento (e-mail, PDF, etc.)
6. Adiciona dados do profissional de saúde
7. Envia relatório e recebe confirmação
