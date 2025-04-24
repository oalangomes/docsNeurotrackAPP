# NeurotrackApp

Organizando o caos com inteligência e empatia.

## ✨ Visão Geral
O NeurotrackApp é um assistente digital projetado para ajudar pessoas neurodivergentes (TDAH, TEA) ou com dificuldades de produtividade e organização.

Ele aprende com o usuário e oferece suporte com:
- Lembretes de medicamentos, consultas e tarefas
- Registro emocional e comportamental
- Análise de padrões via IA
- Divisão de tarefas em etapas menores
- Linha do tempo de evolução

## 📚 Documentação Wiki
A documentação completa do NeurotrackApp está disponível em nossa [Wiki](https://github.com/seu-usuario/neurotrackapp/wiki), que inclui:

- **Casos de Uso**: Fluxos detalhados de todas as funcionalidades, como lembretes e análise de padrões.
- **Arquitetura**: Diagramas C4, fluxos de dados e descrições técnicas.
- **API**: Documentação completa de endpoints, exemplos de requisições e modelos de resposta.
- **Código**: Guias de implementação, estrutura do projeto e melhores práticas.

Para acessar a Wiki, visite: [NeurotrackApp Wiki](https://github.com/seu-usuario/neurotrackapp/wiki).

### Como Contribuir com a Documentação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/neurotrackapp.git
   ```
2. Navegue até a pasta `/docs`:
   ```bash
   cd docs
   ```
3. Faça suas alterações seguindo a estrutura existente.
4. Envie um pull request com suas contribuições.

## 🔧 Tecnologias
- **Backend**: Node.js (v16+)
- **Frontend**: React Native (em desenvolvimento)
- **Banco de dados**: MongoDB
- **IA**: OpenAI
- **Autenticação**: JWT
- **Cache**: Redis

## 📦 Estrutura do Projeto

```
docsNeurotrackAPP/
├── _layouts/           # Layouts para páginas da documentação
├── api/                # Documentação de endpoints da API
├── arquitetura/        # Diagramas e descrições da arquitetura do sistema
├── assets/             # Recursos visuais (imagens, ícones, etc.)
├── casos-uso/          # Casos de uso detalhados
├── codigo/             # Guias e exemplos de código
├── Documents/          # Documentos adicionais relacionados ao projeto
├── _config.yml         # Configuração do site (Jekyll)
├── .gitignore          # Arquivos ignorados pelo Git
├── 404.md              # Página de erro 404 personalizada
├── Gemfile             # Dependências para o Jekyll
├── index.html          # Página inicial do site
├── index.md            # Página inicial em Markdown
└── README.md           # Documentação principal do repositório
```

### Descrição das Pastas e Arquivos
- **_layouts/**: Contém os layouts usados para estruturar as páginas da documentação.
- **api/**: Documentação detalhada dos endpoints da API, incluindo exemplos de requisições e respostas.
- **arquitetura/**: Diagramas e descrições técnicas da arquitetura do sistema.
- **assets/**: Recursos visuais, como imagens e ícones, utilizados na documentação.
- **casos-uso/**: Casos de uso detalhados, explicando fluxos e funcionalidades do sistema.
- **codigo/**: Guias de implementação e exemplos de código para desenvolvedores.
- **Documents/**: Documentos adicionais relacionados ao projeto.
- **_config.yml**: Arquivo de configuração para o Jekyll, usado para gerar o site da documentação.
- **404.md**: Página personalizada para erros 404.
- **Gemfile**: Lista de dependências para o Jekyll.
- **index.html**: Página inicial do site gerado.
- **index.md**: Página inicial em formato Markdown.
- **README.md**: Documento principal com informações gerais sobre o repositório.

## 🚀 Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/neurotrackapp.git
   cd neurotrackapp
   ```

2. Instale as dependências do backend e frontend:
   ```bash
   cd src/backend
   npm install
   cd ../frontend
   npm install
   ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` no diretório `src/backend` com as seguintes variáveis:
     ```
     MONGO_URI=your_mongodb_connection_string
     JWT_SECRET=your_jwt_secret
     ```

4. Inicie o backend e frontend:
   ```bash
   cd src/backend
   npm start
   cd ../frontend
   npm start
   ```

## 🧪 Casos de Uso e Testes
- **Cadastro e login**: Fluxo de autenticação seguro com JWT.
- **Registro diário**: Registro de emoções e comportamentos.
- **Tarefas e subtarefas**: Organização de tarefas em etapas menores.
- **Análise com IA**: Identificação de padrões e sugestões personalizadas.
- **Visualização de progresso**: Linha do tempo para acompanhar a evolução.

## 👨‍💻 Idealizador
**Alan Gomes da Silva**  
Arquiteto de Soluções, +12 anos em tecnologia  
Pai atípico, TDAH e criador do NeurotrackApp

## 📫 Contato
- [LinkedIn](https://www.linkedin.com/in/oalangomes)
- [GitHub](https://github.com/seu-usuario)
- Email: alan.gomes@exemplo.com

## 📝 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
