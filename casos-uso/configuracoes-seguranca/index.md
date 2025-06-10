# Configurações de Segurança

O módulo de Configurações de Segurança do NeurotrackApp permite aos usuários gerenciar aspectos relacionados à proteção de seus dados, autenticação e privacidade, com opções adaptadas às necessidades específicas de pessoas neurodivergentes.

## Diagrama de Fluxo

![Configurações de Segurança](/assets/images/configuracoes_seguranca_consolidado.png)

## Principais Funcionalidades

### Gerenciamento de Autenticação
- **Alteração de senha**: Processo seguro para atualização de credenciais
- **Configuração de biometria**: Habilitação de login por impressão digital ou reconhecimento facial
- **Ativação de autenticação de dois fatores (2FA)**: Camada adicional de segurança
- **Gerenciamento de sessões**: Visualização e encerramento de sessões ativas
- **Histórico de login**: Registro de acessos à conta

### Configurações de Privacidade
- **Definição de visibilidade de dados**: Controle sobre quais informações são compartilhadas
- **Configuração de compartilhamento**: Gerenciamento de permissões para terceiros
- **Gerenciamento de permissões**: Controle de acesso a diferentes funcionalidades
- **Configuração de notificações**: Ajuste de alertas relacionados à segurança
- **Controle de dados sensíveis**: Proteção especial para informações críticas

### Gerenciamento de Dados Pessoais
- **Visualização de dados armazenados**: Acesso a todas as informações pessoais
- **Exportação de dados**: Download de informações em formato portável
- **Exclusão de dados**: Remoção permanente de informações específicas
- **Configuração de backup**: Definição de políticas de cópia de segurança
- **Auditoria de acesso**: Registro de quem acessou os dados

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| PUT | /users/password | Alteração de senha |
| PUT | /users/2fa | Configuração de autenticação de dois fatores |
| GET | /users/sessions | Listagem de sessões ativas |
| DELETE | /users/sessions/{id} | Encerramento de sessão específica |
| PUT | /users/privacy | Atualização de configurações de privacidade |
| GET | /users/data | Exportação de dados pessoais |
| DELETE | /users/data | Exclusão de dados específicos |
| PUT | /users/backup | Configuração de backup |

## Cenários de Uso

### Ativação de Autenticação de Dois Fatores
1. Usuário acessa a seção de Configurações de Segurança
2. Seleciona a opção de autenticação de dois fatores
3. Escolhe o método preferido (SMS, e-mail, aplicativo autenticador)
4. Sistema envia código de verificação pelo método escolhido
5. Usuário insere o código para confirmar
6. Sistema ativa 2FA e fornece códigos de recuperação
7. Usuário salva os códigos de recuperação em local seguro
8. Recebe confirmação de ativação bem-sucedida

### Gerenciamento de Permissões de Compartilhamento
1. Usuário acessa configurações de privacidade
2. Visualiza lista de pessoas/aplicativos com acesso aos seus dados
3. Seleciona um contato específico para ajustar permissões
4. Define quais módulos podem ser acessados (ex: medicação, humor)
5. Configura nível de detalhe das informações compartilhadas
6. Define período de validade do acesso
7. Salva as configurações e recebe confirmação

### Exportação de Dados Pessoais
1. Usuário acessa gerenciamento de dados pessoais
2. Seleciona opção de exportar dados
3. Escolhe quais tipos de dados deseja incluir
4. Define formato de exportação (JSON, CSV, PDF)
5. Sistema processa a solicitação e prepara o arquivo
6. Usuário recebe notificação quando o arquivo está pronto
7. Faz download dos dados em formato estruturado e portável
