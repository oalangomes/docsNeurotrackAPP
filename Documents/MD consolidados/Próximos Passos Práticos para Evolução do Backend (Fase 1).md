## Próximos Passos Práticos para Evolução do Backend (Fase 1)

Com base na arquitetura atual do seu backend Node.js e no planejamento evolutivo que discutimos, aqui estão os passos práticos recomendados para iniciar a **Fase 1: Fortalecimento do Monolito Modular e Introdução de Filas**:

### A. Fortalecer o Monolito Modular

O objetivo aqui é melhorar a organização interna do código existente, facilitando a manutenção e futuras evoluções, sem alterar a funcionalidade externa imediatamente.

1.  **Revisão de Acoplamento e Definição de Interfaces:**
    *   **Ação:** Analise as chamadas diretas entre os diferentes serviços (`src/services`). Por exemplo, verifique onde `taskService.js` chama diretamente `aiService.js` ou `googleCalendarService.js`.
    *   **Objetivo:** Identificar pontos onde a comunicação poderia ser mais desacoplada. Comece a definir interfaces claras (usando TypeScript ou JSDoc) para os métodos públicos de cada serviço.
    *   **Exemplo Prático:** Documente formalmente os métodos que `aiService` expõe e garanta que outros serviços o utilizem apenas através dessa interface documentada.

2.  **Melhoria da Documentação Interna (JSDoc):**
    *   **Ação:** Adicione blocos de comentários JSDoc aos principais serviços (`authService`, `userService`, `taskService`, `dailyEntryService`, `aiService`, etc.) e modelos (`src/models`).
    *   **Objetivo:** Explicar o propósito de cada módulo, seus métodos públicos, parâmetros e o que retornam. Isso melhora a compreensão e facilita a manutenção.

3.  **Aumento da Cobertura de Testes Unitários:**
    *   **Ação:** Comece a escrever testes unitários (usando Jest, Mocha, ou o framework de sua preferência) para as funções críticas dentro dos serviços, especialmente aquelas com lógica de negócio complexa.
    *   **Objetivo:** Garantir que as regras de negócio funcionem como esperado e que futuras refatorações não introduzam regressões. Foque inicialmente nos serviços mais utilizados.
    *   **Exemplo Prático:** Crie testes para as funções de validação em `authService`, para a lógica de criação/atualização em `taskService`, etc.

### B. Introduzir Filas e Processamento Assíncrono

O objetivo é mover operações lentas ou que não precisam de resposta imediata para serem processadas em background, melhorando a performance percebida pelo usuário e a resiliência do sistema.

1.  **Configuração do Sistema de Filas (BullMQ + Redis):**
    *   **Ação:** Instale a biblioteca `bullmq` (`npm install bullmq`).
    *   **Ação:** Verifique e ajuste a configuração do Redis (`config/redisClient.js`) para ser usada pelo BullMQ. O Redis atuará como o backend da fila.
    *   **Ação:** Crie uma nova estrutura de diretórios, por exemplo, `src/queues` para definir as filas (ex: `aiQueue.js`, `calendarQueue.js`) e `src/workers` para os processadores de jobs (ex: `aiWorker.js`, `calendarWorker.js`).

2.  **Refatorar a Geração de Resposta da IA (`POST /ai/generate-response`):**
    *   **Ação:** Modifique o controller `aiController.js` (`generateResponse`). Em vez de chamar `aiService.generateResponse` e esperar, ele deve:
        1.  Criar um *job* contendo os dados necessários (prompt, contexto, userId) e adicioná-lo à `aiQueue`.
        2.  Retornar uma resposta imediata ao usuário, como `HTTP 202 Accepted`, talvez incluindo um ID de job para rastreamento.
    *   **Ação:** Crie o `aiWorker.js`. Este worker irá escutar a `aiQueue`, pegar os jobs, chamar o `aiService.generateResponse` original, e lidar com o resultado (armazenar, notificar, etc.).

3.  **Refatorar a Sincronização com Google Calendar:**
    *   **Ação:** Identifique os locais onde o `googleCalendarService` é chamado (provavelmente em `calendarController.js` e talvez em `taskService.js` ao criar/atualizar tarefas com data).
    *   **Ação:** Modifique esses locais para, em vez de chamar o serviço diretamente, criar um *job* na `calendarQueue` com os dados necessários.
    *   **Ação:** Crie o `calendarWorker.js` para processar esses jobs de sincronização em background.

4.  **Implementar Mecanismo de Feedback (WebSockets):**
    *   **Ação:** Integre uma biblioteca de WebSockets como `socket.io` ao seu servidor Express.
    *   **Ação:** Implemente a lógica para que, quando um usuário se conecta, ele entre em uma 
