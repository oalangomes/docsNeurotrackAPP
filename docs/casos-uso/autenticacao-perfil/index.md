# Autenticação e Perfil

O módulo de Autenticação e Perfil do NeurotrackApp gerencia todo o processo de login, cadastro e configuração do perfil do usuário, com foco especial nas necessidades de pessoas neurodivergentes.

## Diagrama de Fluxo

![Autenticação e Perfil](../assets/images/autenticacao_perfil_consolidado.png)

## Principais Funcionalidades

### Autenticação
- **Múltiplas opções de login**: E-mail/senha, Google, biometria
- **Cadastro simplificado**: Processo otimizado para minimizar sobrecarga cognitiva
- **Recuperação de senha**: Fluxo intuitivo para redefinição de credenciais
- **Autenticação de dois fatores**: Camada adicional de segurança opcional

### Perfil de Usuário
- **Configuração de perfil neurodivergente**: Identificação de condições específicas (TDAH, TEA, etc.)
- **Preferências de interação**: Ajustes na forma como o aplicativo se comunica com o usuário
- **Dados pessoais**: Gerenciamento de informações básicas e contatos de emergência

### Gerenciamento de Conta
- **Visualização e edição de dados**: Interface simplificada para atualização de informações
- **Atualização de senha**: Processo seguro para alteração de credenciais
- **Edição de perfil neurodivergente**: Ajustes nas configurações específicas para necessidades do usuário
- **Gerenciamento de preferências**: Personalização da experiência do usuário

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /auth/register | Cadastro de novo usuário |
| POST | /auth/login | Autenticação de usuário |
| POST | /auth/refresh-token | Renovação de token de acesso |
| POST | /auth/forgot-password | Solicitação de recuperação de senha |
| POST | /auth/reset-password | Redefinição de senha |
| GET | /users/profile | Obtenção de dados do perfil |
| PUT | /users/profile | Atualização de dados do perfil |
| PUT | /users/neuro-profile | Atualização de perfil neurodivergente |
| PUT | /users/preferences | Atualização de preferências |
| DELETE | /users/account | Exclusão de conta |

## Cenários de Uso

### Cadastro de Novo Usuário
1. Usuário acessa a tela de cadastro
2. Preenche dados básicos (nome, e-mail, senha)
3. Opcionalmente configura perfil neurodivergente
4. Define preferências iniciais de interação
5. Confirma cadastro e recebe confirmação

### Login com Biometria
1. Usuário seleciona opção de login com biometria
2. Sistema solicita autenticação biométrica
3. Após validação, usuário é autenticado e redirecionado para a Home

### Atualização de Perfil Neurodivergente
1. Usuário acessa configurações de perfil
2. Seleciona opção de perfil neurodivergente
3. Ajusta configurações específicas para sua condição
4. Salva alterações e recebe confirmação
