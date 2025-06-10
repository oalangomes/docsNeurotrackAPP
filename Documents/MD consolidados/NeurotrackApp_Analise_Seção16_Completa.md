# Seção 16 – Arquitetura Técnica e Visão de Futuro (IA Própria, Embarcada, Integrações)

---

## 1. Arquitetura Atual (MVP)

### Backend
- Node.js + Express
- MongoDB com Mongoose
- Redis (cache, sessões, TTL adaptativo)
- JWT para autenticação
- Swagger para documentação
- Middleware IA com cache e contexto básico (OpenAI)
- Testes com Jest e Supertest (alvo mínimo: 65%)

### Frontend
- React Native
- Layout responsivo e acessível
- Estilo validado para neurodivergência

---

## 2. Componentes Técnicos Relevantes

- Modularização por domínio (controllers, services, middlewares)
- Rate limiting e segurança com Redis
- Integração Google Calendar com OAuth2
- Mensagens multilíngues via messages.js
- Swagger com geração automática + export `.md` para GitHub
- GitHub Actions com Redis e Mongo em CI

---

## 3. Visão de Evolução Arquitetural (Pós-MVP)

### Etapa 1 – IA Aberta com Middleware Otimizado
- Middleware com:
  - Cache semântico com embeddings
  - TTL adaptativo por tipo de pergunta
  - Histórico por usuário
  - Tagging automático
  - IA com awareness de rotina, emoções e contexto

### Etapa 2 – Integrações com Dispositivos e Serviços
- Alexa (Skill personalizada com OAuth)
- Apple Health, Google Fit (dados de sono, passos, batimentos)
- Integração com calendários institucionais (Google/Microsoft)
- API institucional para clínicas e escolas
- Acesso por geolocalização para acionar rotinas

### Etapa 3 – IA Embarcada Adaptativa (via Hugging Face / Ollama)
- LLM open-source rodando localmente
- Embeddings por usuário armazenados em Redis/Vespa/Weaviate
- Treinamento leve com consentimento (fine-tuning por cluster de perfil)
- IA responde com base em perfil real, humor, rotina e feedbacks anteriores

### Etapa 4 – IA Própria Neurotrack (Privada e Especializada)
- Treinamento com dados consentidos de perfis neurodivergentes
- Otimizada para linguagem emocional, organização pessoal, acolhimento e autonomia
- Geração de contexto para múltiplos usuários de forma ética, transparente e adaptável
- Capaz de operar com ou sem conexão (modo offline embarcado leve)

---

## 4. Estrutura Final Esperada

### Backend
- Microsserviços ou estrutura modular escalável
- IA embarcada integrada com fallback para OpenAI
- Fila de background para IA lenta e notificações preditivas (BullMQ)
- MongoDB + VetorDB (ex: Weaviate, Qdrant) para embeddings
- Autenticação multifator
- API Gateway com controle de versão

### Frontend
- React Native com modo acessível, dark mode e modo “crise”
- Suporte a voz, gesto e leitura de tela
- Ações rápidas direto da notificação (Android/iOS nativo)

### Infra
- Docker + Docker Compose para dev local e staging
- Deploy em VPS escalável ou container em nuvem
- Monitoramento com Grafana + Loki ou Elastic Stack
- CDN para entrega rápida do app

---

## 5. Considerações Finais

O NeurotrackApp está sendo projetado para crescer de forma modular, com base sólida no presente e com suporte a IA embarcada, integração com dispositivos inteligentes e privacidade controlada pelo usuário. Ele se torna mais do que um app: uma extensão adaptativa da mente e rotina neurodivergente.