# NeurotrackApp - Consolidação Completa de Funcionalidades, Análises e Anotações (v2)

## Introdução

Este documento representa a consolidação mais recente do escopo funcional, análises detalhadas, sugestões técnicas, histórias de usuário e anotações relevantes para o projeto NeurotrackApp. Ele integra as informações do escopo inicial com as análises aprofundadas realizadas posteriormente, fornecendo uma visão unificada e detalhada do projeto, abrangendo o Produto Mínimo Viável (MVP) e as fases Pós-MVP.

---

## ✅ MVP - Funcionalidades Essenciais Consolidadas

Esta seção agrupa as funcionalidades essenciais para o MVP, enriquecidas com detalhes das análises.

### 1. Cadastro, Autenticação e Perfil do Usuário (Baseado na Análise Seção 1)

- **Criação de Conta:**
    - Permitir cadastro utilizando e-mail e senha, com validações adequadas.
    - Suporte para login social via Google (OAuth) para praticidade.
    - **Sugestão:** Validação de e-mail com envio de token antes do primeiro login para segurança.
    - *História:* "Como jovem com TDAH, quero entrar rápido com Google para não desistir."
- **Autenticação:**
    - Implementar login seguro utilizando JSON Web Tokens (JWT).
    - **Sugestão:** Avaliar uso de refresh tokens (HttpOnly) para sessões longas.
    - *História:* "Como pai acessando à noite, quero sessão longa para não logar toda hora."
- **Preenchimento de Perfil Complementar:**
    - Solicitar nome, idade/data de nascimento, idioma, gênero (opcional) após cadastro inicial.
    - **Comentário:** Onboarding progressivo é recomendado.
    - *História:* "Como pessoa com TEA, fico ansiosa com cadastros longos. Quero preencher aos poucos."
- **Perfil Neurodivergente:**
    - Coletar diagnósticos (TDAH, TEA, etc. - permitir múltiplos), sintomas e estágio (condicional ao diagnóstico).
    - **Sugestão:** Adicionar tooltips explicativos.
    - *História:* "Como mãe de criança com TDAH e TEA, quero informar ambos para ajustar sugestões."
- **Detecção Automática:**
    - Inferir status "Neurodivergente?" e "Tipo de Perfil" via lógica no backend.
    - **Comentário:** Essencial testar casos ambíguos.
    - *História:* "Como adolescente em investigação, quero ser identificado como potencial neurodivergente mesmo sem diagnóstico fechado."
- **Gestão de Dependentes:**
    - Permitir vincular responsáveis e dependentes.
    - **Comentário:** Backend precisa lidar com permissões e múltiplos perfis.
    - *História:* "Como pai de duas crianças neurodivergentes, quero ver progresso separado e comparar rotinas."
- **Resumo Final:**
    - Apresentar tela de resumo ao final do cadastro/perfil.
    - **Sugestão:** Permitir edição antes de confirmar.
    - *História:* "Como mãe atarefada, quero revisar dados dos filhos antes de finalizar."
- **Segurança da Conta (MVP inicial):**
    - Incluir logout.
    - **Comentário:** Planejar exclusão de conta e recuperação de senha desde já.
    - *História:* "Como jovem que compartilha celular, quero sair fácil para ninguém ver meus registros."

### 2. Entrada Diária (Journaling) (Baseado na Análise Seção 2 e Aprimoramento Diário Seguro)

- **Registro Diário:**
    - Permitir registro de eventos, humor (emojis), foco, energia, reflexões, sentimentos, desabafos.
    - **Aprimoramento:** Incluir campo "Situação" (Reflexão, Risco, Pensamento Intrusivo, Crise, Desabafo, Positivo) para contextualizar a entrada.
    - **Sugestão:** Navegação rápida por categorias, geotag/tags de horário futuras.
    - *História:* "Como adolescente com TDAH/TEA, quero registrar humor com emojis, é mais fácil."
    - *História (Situação):* "Como jovem com pensamentos agressivos, quero marcar como risco para IA acolher com cuidado."
- **Histórico:**
    - Visualização cronológica.
    - **Sugestão:** Expandir para filtros (humor, tags, período), calendário emocional visual.
    - *História:* "Como paciente em terapia, quero mostrar ao psicólogo meu histórico das últimas semanas."
- **Sugestões da IA:**
    - Integrar com OpenAI para sugestões automáticas (respostas, tarefas, acolhimento) baseadas no texto e histórico.
    - **Comentário:** Reações empáticas e adaptadas, prever fallback offline, latência, controle de tom.
    - **Aprimoramento (Diário Seguro):** IA só analisa entradas protegidas/sensíveis com autorização explícita e foco em risco (ideação suicida, agressividade). Resposta cuidadosa: "Percebi que este relato pode ser difícil. Quer conversar ou uma sugestão acolhedora?"
    - *História:* "Como mulher com sobrecarga, quero que IA sugira algo gentil quando estou esgotada."
    - *História (Diário Seguro):* "Como mãe no limite, quero escrever livremente, só quero intervenção se detectar risco."
- **Privacidade e Segurança:**
    - Garantir criptografia dos dados.
    - Exibir avisos claros: “Conteúdo criptografado e privado.”
    - **Aprimoramento (Diário Seguro):** Permitir marcar entrada como "Protegida" (senha/biometria extra) ou "Sensível" (não indexada pela IA). Flags `exportable: false`, `private: true`, `allowAI: false` (padrão se sensível), `riskAnalyzed: false` (até autorizar).
    - **Sugestão:** Permitir exportação segura e exclusão individual.
    - *História:* "Como adolescente com traumas, quero garantir que ninguém acesse esses registros, mesmo com celular desbloqueado."

### 3. Gerenciamento de Tarefas (Baseado na Análise Seção 3 e Lista de Compras)

- **CRUD Completo:** Criação, visualização, edição, exclusão.
    - **Sugestão:** Soft delete para manter histórico.
- **Campos da Tarefa:** Título, descrição, datas (início/fim), prioridade, status, tags sensoriais, nível de energia.
    - **Comentário:** Nível de energia e tags sensoriais são diferenciais.
    - *História:* "Como adulto neurodivergente, quero saber se tarefa exige muita energia/exposição sensorial."
- **Quebra de Tarefas (Subtarefas):**
    - Opção de dividir tarefas complexas.
    - **Comentário:** Útil para quem sente bloqueio.
    - *História:* "Como mãe com TDAH, quero dividir tarefas grandes para não travar."
- **Marcação de Conclusão:** Essencial para progresso.
    - **Sugestão:** Pode alimentar gamificação.
- **Visualização:** Listar por dia, agrupar por status/data.
    - **Sugestão:** Filtro por energia/tipo/tag, ícones/cores.
- **Sugestões da IA:** Resumo de tarefas, foco, organização baseada no perfil (`/ai/summarize-tasks`).
    - **Comentário:** IA pode sugerir ordem de execução.
- **Interface Padronizada:** Modal com campos de linha única, ícones azuis, seguindo guia visual.
- **Designação Futura:** Backend pronto (`assignedTo`).
- **Uso como Lista de Compras (MVP Mínimo):**
    - Possível usar tarefa "Lista Mercado" com itens como subtarefas.
    - **Limitações:** Sem quantidade, edição não otimizada, sem categorias, sem reutilização.
    - *História:* "Como pessoa que esquece itens, quero criar tarefa com subtarefas para cada item, marcando conforme compro."
    - **Sugestão Pós-MVP (Lista de Compras):** Tipo especial "Lista de Compras", itens com quantidade, IA para extrair de frases, listas frequentes, compartilhamento, agrupamento.
- **Notificações com Ação Direta (Integração Seção 15):** Concluir/Adiar direto da notificação.

### 4. Chat IA Personalizado (Baseado na Análise Seção 4)

- **Interface de Chat:** Estilo bolha, scroll automático, diferenciação visual, botões acessíveis.
    - **Sugestão:** Favoritar/resgatar mensagens.
    - *História:* "Como pessoa que usa à noite, quero interface clara e sem ruídos."
- **Integração com OpenAI:** Definir modelo (GPT-3.5/4), tokens, fallback, cache, limitação, custo.
    - *História:* "Como estudante com TDAH/ansiedade, quero conversar sobre sentimentos e ter resposta empática."
- **Contextualização:** Adaptar respostas (vocabulário, abordagem) com base no perfil, histórico (persistente), contexto da conversa.
    - **Comentário:** Núcleo da proposta, respeito à privacidade.
    - *História:* "Como mãe de criança com TEA, quero que IA responda com empatia e exemplos práticos."
- **Histórico:** Manter histórico (backend criptografado), opção de apagar.
    - **Sugestão:** Busca por termos futura.
    - *História:* "Como pessoa que usou IA para dicas, quero reler respostas anteriores sem repetir pergunta."
- **Feedback Visual:** Indicador "digitando...", animação leve, fallback para erro.
    - *História:* "Como adolescente com ansiedade, ver 'digitando...' me acalma."
- **Middleware Inteligente (MVP inicial):** Cache Redis (prompts/respostas, histórico), estrutura para evoluções (tagging, similaridade, TTL adaptativo, embeddings, NLP).
    - *História:* "Como usuário recorrente, quero que IA lembre perguntas anteriores e mostre dicas relacionadas."

### 5. Integração com Agenda (Google Calendar) (Baseado na Análise Seção 5 e Integração Tarefas)

- **CRUD de Eventos Locais:** Criação, visualização, edição, exclusão no app.
    - **Sugestão:** Diferenciar visualmente evento x tarefa.
    - *História:* "Como pessoa que confunde tarefas e compromissos, quero ver claramente o que é reunião e o que é tarefa."
- **Sincronização com Google Calendar:**
    - Integração via OAuth2 (escopo `calendar.events`).
    - Mapeamento com UID local, token seguro, detecção de conflitos.
    - *História:* "Como adulto com TDAH, quero ver no Google Calendar o que registrei no app."
- **Visualização no App:**
    - Exibir eventos da agenda.
    - **Sugestão:** Calendário visual (ícones, cor por origem), alternância diário/semana/mês.
    - *História:* "Como jovem com TEA, quero ver agenda visual com ícones."
- **Conexão com Tarefas (Recomendação Híbrida):**
    - Tarefas com data+hora → Evento no Google Calendar.
    - Tarefas sem hora → Ficam no app.
    - Botão opcional: "Adicionar ao Google Agenda".
    - **Comentário:** Evita poluir calendário, dá controle ao usuário.
    - *História:* "Quando marco tarefa para 14h, quero que apareça no Google Agenda com lembrete."
- **Privacidade e Controle:**
    - Permitir ativar/desativar sincronização.
    - Controle sobre qual evento enviar.
    - *História:* "Como terapeuta, quero compromissos visíveis só na agenda pessoal."

### 6. Tela Home e Resumo Final (Baseado na Análise Seção 6)

- **Dashboard Diário:** Resumo visual do dia (tarefas pendentes, última entrada, eventos, sugestões IA).
    - **Sugestão:** Seções colapsáveis, visual limpo, destaques suaves.
    - *História:* "Como pessoa com TDAH, quero abrir e ver tudo do dia numa tela."
- **Navegação:** Acesso rápido às funções principais (Bottom tab/ícones).
    - **Sugestão:** Indicadores visuais, botão flutuante.
    - *História:* "Como mãe, quero acessar rápido tarefas e entradas."
- **Interface:** Layout limpo, acessível, intuitivo. Mensagens personalizadas da IA na Home.
    - **Comentário:** Personalização na Home é diferencial.
    - *História:* "Como pessoa perdida ao iniciar o dia, quero mensagem acolhedora e guia prático."

---

## 🔄 Pós-MVP - Funcionalidades Complementares e Futuras

Esta seção detalha funcionalidades planejadas para fases posteriores, enriquecidas com análises.

### 7. Gestão de Medicação (Baseado na Análise Seção 7 e Medicação como Tarefa)

- **CRUD de Medicações:** Cadastro, edição, exclusão (nome, dose, horários, frequência).
    - **Sugestão:** Incluir tipo, via, instruções extras, autoformatação de unidade.
    - *História:* "Como pai, quero registrar doses e horários corretamente para evitar erros."
- **Lembretes:** Visuais/notificações.
    - **Sugestão:** Múltiplos horários, som, vibração, persistência, integração futura com voz.
    - *História:* "Como mulher com TDAH, esqueço remédio. Quero notificação clara e persistente."
- **Registro de Uso:** Marcar como tomada (check).
    - **Comentário:** Permite visualização diária, marcação com justificativa ("não tomado - efeito colateral").
    - *História:* "Como adolescente, quero marcar se tomei para acompanhar minha responsabilidade."
- **Histórico e Relatórios:** Visualizar histórico de adesão.
    - **Sugestão:** Relatórios (%, lista, exportação CSV/PDF), visual gráfico.
    - *História:* "Como mãe, quero exportar relatório para mostrar na consulta."
- **Integração com Diário (Futuro):** Relacionar tomada com efeitos percebidos.
    - **Comentário:** IA pode correlacionar timestamps e gerar insights (ex: sonolência após uso).
    - *História:* "Como TO, quero ver se humor/foco é afetado por medicação específica."
- **Estratégia de Integração (Medicação como Tarefa):**
    - Cadastro de medicação gera tarefas recorrentes (visíveis/invisíveis) para lembretes centralizados.
    - Título: "Tomar [Remédio] - [Hora]", Tags: `medicação`, `noturno`, etc.
    - Registro de uso permanece no módulo Medicação, mas pode marcar tarefa como concluída.
    - **Conclusão:** Aumenta eficácia dos lembretes sem perder controle específico de adesão.

### 8. Preferências Avançadas e Personalização (Baseado na Análise Seção 8)

- **Ajustes da IA:** Ajustar tom (empático, técnico, lúdico, objetivo), estilo de resposta.
    - **Sugestão:** Ajustes temporários por sessão.
    - *História:* "Como jovem com TDAH, às vezes quero respostas objetivas, outras vezes acolhedoras."
- **Configurações de Perfil:** Expandir para estilo de aprendizado (visual, auditivo, cinestésico), sensibilidades sensoriais, preferências de rotina, filtros para sugestões.
    - **Comentário:** Sensibilidades afetam sugestões (ex: evitar locais barulhentos).
    - *História:* "Como criança TEA com hipersensibilidade, quero que app evite sugerir tarefas em ambientes barulhentos."
- **Temas Visuais:** Opções Claro/Escuro/Sistema, complexidade visual (Mínima/Média).
    - **Sugestão:** Preview, agendamento de modo escuro.
    - *História:* "Como pessoa com TEA, me distraio fácil. Quero interface limpa."
- **Alertas e Feedback:** Configurar sons (Suaves/Nenhum), feedback tátil.
    - **Sugestão:** Teste de som/vibração.
    - *História:* "Como criança com hipersensibilidade auditiva, quero só alertas visuais ou vibração leve."
- **Contextos Adaptativos (Futuro):** Adaptar interface/sugestões ao momento do dia (manhã=foco, noite=relaxamento).
    - **Comentário:** Integra com rotina, energia, diário.
    - *História:* "Como adulto com TDAH, quero que IA ajude a organizar minha manhã."

### 9. Configurações de Segurança e Conta (Baseado na Análise Seção 9)

- **Recuperação de Senha:** Fluxo completo (solicitação, token seguro via e-mail, página de redefinição).
    - *História:* "Como pai, esqueço senhas. Quero recuperar acesso rápido."
- **Atualização de Dados (e-mail):** Permitir atualização com autenticação e verificação do novo e-mail.
    - *História:* "Como mãe que trocou de e-mail, quero atualizar sem perder histórico."
- **Termos de Uso:** Modal no primeiro acesso/atualização, scroll obrigatório, checkbox, registro de aceite.
    - *História:* "Como usuária cuidadosa, quero saber o que aceito e revisar termos."
- **Autenticação Multifator (MFA) – Futuro:**
    - **Sugestão Inicial:** 2FA via e-mail (token/link mágico). Futuro: Apps Authenticator.
    - *História:* "Como terapeuta, quero camada extra de segurança."
- **Exclusão de Conta:** Opção de deletar conta.
    - **Sugestão:** Confirmação com senha, aviso claro, soft delete (recuperação 30 dias), logs.
    - *História:* "Como adolescente testando, quero poder excluir conta com garantia que dados sumirão."

### 10. Análises, Relatórios e Estatísticas (Baseado na Análise Seção 10)

- **Dashboards Pessoais:** Visualizações gráficas (humor, foco, energia, tarefas) por período.
    - **Sugestão:** Visão simples (emojis/barras) e detalhada (linhas/radar), seleção de período/métrica.
    - *História:* "Como adulto com TDAH, quero ver dias de baixa energia e impacto na produtividade."
- **Insights da IA:** Geração automática de padrões com sugestões empáticas.
    - **Comentário:** Opcional, com consentimento.
    - *História:* "Como jovem com TEA, quero insights só se pedir e que sejam acolhedores."
- **Exportação:** Exportar dados/relatórios (CSV, JSON, PDF).
    - **Sugestão:** Filtros por período, tipo de dado, formato.
    - *História:* "Como terapeuta, quero relatório mensal (humor, energia, tarefas, medicações) para ajustar plano."
- **Comparativos:** Comparativo de tarefas concluídas por semana.
    - **Sugestão:** Comparação com médias, reforços positivos.
    - *História:* "Como pessoa que se cobra, quero acompanhar evolução sem culpa nas semanas ruins."
- **Sugestões Futuras:** Sistema de pontuação, Relatório Pessoal vs. Clínico, Alertas inteligentes.

### 11. Rotinas e Hábitos (Baseado na Análise Seção 11)

- **Criação de Rotinas:** Definição de rotinas visuais (diárias/semanais).
    - **Sugestão:** Blocos visuais, modelos reutilizáveis (matinal, noturna, fim de semana).
    - *História:* "Como criança com TEA, me sinto segura com rotina com horários e imagens claras."
- **Checklist de Hábitos:** Acompanhar hábitos diários.
    - **Comentário:** Tracker simples, reforço positivo, frequência.
    - *História:* "Como adulto com TDAH, quero checklist diário para manter hábitos, porque esqueço fácil."
- **Integração:** Conectar rotinas com lembretes, tarefas, agenda.
    - **Comentário:** Hábito → tarefa recorrente → lembrete.
    - *História:* "Como mãe, quero colocar 'escovar dentes' como hábito com reforço visual e ativação na hora certa."
- **Gamificação (Streak):** Reforço positivo para manutenção (streaks).
    - **Sugestão:** Barras de progresso, frases motivacionais, notificações de conquista.
    - *História:* "Como adolescente com TDAH, fico motivada vendo que mantenho hábitos em sequência."
- **Sugestões Contextuais por Localização (Futuro - Ver Seção 14):** Ativar rotinas/hábitos por localização.
- **Sugestões Futuras:** Modelos prontos (TEA, TDAH), compartilhamento, mensagens de reforço após falhas, rotinas adaptativas (baseadas em emoção/energia).

### 12. Gamificação e Engajamento (Baseado na Análise Seção 12)

- **Sistema de Pontos:** Pontos por consistência e conclusão (tarefas, hábitos, registros).
    - **Comentário:** Sistema simples, metas visuais, sem comparação externa.
    - *História:* "Como criança com TDAH, quero ganhar pontos ao fazer tarefas, me dá sensação de vitória."
- **Recompensas:** Medalhas, feedbacks positivos, avatares desbloqueáveis.
    - **Sugestão:** Sala de conquistas.
    - *História:* "Como adolescente com baixa autoestima, quero ver avanços como medalhas para lembrar que evoluo."
- **Desafios:** Desafios semanais propostos pela IA (personalizados, alcançáveis).
    - **Comentário:** Recompensas simbólicas ao completar.
    - *História:* "Como adulto que procrastina, quero pequenos desafios para manter ritmo."
- **Modo Imersivo (Foco):** Modo de foco com sons, timers, modo escuro.
    - **Sugestão:** Timer Pomodoro, sons ambientes, interface mínima.
    - *História:* "Como jovem com TEA, me acalmo com sons suaves. Quero ativar modo para fazer tarefas que travo."
- **Sugestões Futuras:** Missões de longo prazo, ritual noturno, feedback na Home, modo gamificação opcional.

### 13. Compartilhamento e Colaboração (Baseado na Análise Seção 13)

- **Acesso Multiusuário (Responsáveis/Dependentes):** Responsável alterna entre perfis vinculados, permissões distintas.
    - *História:* "Como pai, quero acompanhar cada filho com perfis separados."
- **Compartilhamento com Profissionais:** Compartilhamento seguro (link/token temporário com escopo definido) de dados/relatórios.
    - **Comentário:** Ideal para profissionais que não usam o app, permissões de leitura restrita.
    - *História:* "Como terapeuta, quero receber link temporário com relatório do mês, sem baixar app."
- **Planos de Atividades Compartilhados (Futuro):** Criar/compartilhar planos customizados, acesso a repositório.
    - **Sugestão:** Biblioteca por perfil/idade/diagnóstico, adaptação automática.
    - *História:* "Como mãe, quero baixar plano de rotina recomendado e adaptar para minha filha."
- **Gestão Multiusuário Avançada (Expansão):**
    - Perfis Hierárquicos: Administrador, Responsável Secundário, Profissional/Observador.
    - Gerenciamento por Convite: E-mail/token com validade/escopo.
    - Logs e Auditoria: Histórico de acessos, acesso revogável.
    - *História:* "Como mãe principal, quero controlar quem acessa perfis dos filhos e dar acesso temporário à terapeuta."
- **Sugestões Futuras:** Mensagens seguras pais/profissionais, assinatura digital, área privada para anotações profissionais, auditoria.

### 14. Integrações Adicionais (Baseado na Análise Seção 14 e Geolocalização)

- **Microsoft Calendar:** Integrar via Microsoft Graph API (OAuth2, UIDs, escopo mínimo).
    - *História:* "Como professora, quero sincronizar compromissos do aluno com meu Outlook."
- **Alexa (Skill):** Desenvolver Skill para interação por voz (ver agenda, registrar diário, lembrar medicação).
    - *História:* "Como pai de criança que prefere falar, quero que ela use Alexa para registrar rotina."
- **Apple Calendar / Apple Health / Google Fit / Wearables:** Sincronizar dados de saúde (sono, passos, batimentos, atividade).
    - **Comentário:** Análise cruzada com foco/energia/humor. IA pode gerar insights ("sono > 7h → foco +30%").
    - *História:* "Como jovem com TDAH, quero ver se dormir bem melhora meu foco comparando com smartwatch."
- **Notificações Push (FCM/APNS):** Notificações preditivas e com ações diretas.
    - **Exemplos:** Tarefa [Concluir/Adiar], Sugestão IA [Aceitar/Recusar], Reengajamento ("Esqueceu diário?").
    - *História:* "Como pessoa que esquece, quero lembretes simples com ações rápidas na notificação."
- **Geolocalização Contextual (Pós-MVP, Prioridade Média/Baixa):**
    - Usar localização para ativar rotinas/lembretes (requer permissão background location, geofencing, POIs/Places API).
    - **Cenário Farmácia:** Entrou na farmácia → Alerta sobre tarefas/medicamentos pendentes (tags: saúde, remédio; palavras-chave: nomes de remédios).
    - **Cenário Mercado:** Entrou no mercado → Alerta sobre itens pendentes em tarefas tipo "Lista de Compras" (identificada por título, tag ou subtarefas).
    - **Dependências/Restrições:** Consumo de bateria, precisão da localização, privacidade, limitações do SO, qualidade dos POIs, complexidade de implementação/testes.
    - **Recomendação:** Manter Pós-MVP, prioridade média/baixa. Abordagem faseada (locais manuais primeiro, depois detecção automática).
    - *História (Farmácia):* "Lembrete útil ao entrar na farmácia para não esquecer remédios."
    - *História (Mercado):* "Lembrete ao chegar no mercado para consultar lista e evitar esquecimentos."
    - *História (Geral):* "Como mãe sobrecarregada, quero que app lembre coisas importantes baseado em onde estou."
- **Sugestões Futuras:** Integração calendário escolar, exportação sistemas de saúde, API institucional.

### 15. Funcionalidades Avançadas Inteligentes (Baseado na Análise Seção 15)

- **Ações Diretas nas Notificações:** Botões [Concluir]/[Lembrar mais tarde] para tarefas; [Aceitar]/[Recusar] para sugestões IA.
- **IA Própria Adaptativa:** Evolução planejada (OpenAI → open-source → IA Neurotrack) com núcleo comum + perfil usuário, sugestões mais humanas, tom ajustado.
- **Memória Contextual da IA:** IA lembra preferências, rotinas, emoções passadas (com consentimento). Ex: “Na última vez que falou sobre isso, estava nervoso. Quer aquela sugestão que funcionou?”
- **Diário com Gravação de Áudio:** Entrada por voz com transcrição automática (ou só voz). Ideal para crises, crianças, TEA.
- **Rotina Guiada com Imagens:** Passo a passo visual/falado. Ex: “Hora de escovar os dentes. Toque quando terminar.” Ativável por responsáveis ou automático.
- **Agenda Visual:** Emojis, cores, ícones por tipo de atividade. Modo arrastar/soltar.
- **Modo de Acessibilidade (PRIORIDADE):** Modo para TEA, TDAH, dislexia, baixa visão, sobrecarga. Ajustes: redução estímulos, layout mínimo, leitura em voz alta, tempo ampliado, linguagem simples. Ativação no onboarding ou menu.

---

## ⚙️ Anotações Técnicas e Observações Consolidadas

Esta seção reúne observações técnicas, decisões de arquitetura, tecnologias, padrões de UI/UX e outros detalhes relevantes mencionados nos documentos de escopo e análises.

### Tecnologias Principais
- **Backend:** Node.js com Express.js.
- **Frontend:** React Native.
- **Banco de Dados:** MongoDB (Mongoose). `MongoMemoryServer` para testes.
- **Cache:** Redis (prompts IA, histórico, sessão, rate limiting). TTL fixo/adaptativo, planos para cache semântico.
- **IA:** OpenAI (GPT-3.5/4) inicialmente. Planos: open-source (LLama 3, Mistral), modelo próprio futuro.

### Arquitetura e Padrões de Backend
- **Estrutura:** Modular (`controllers`, `services`, `middlewares`).
- **Autenticação:** JWT.
- **Validação:** Joi (multilíngue).
- **API:** RESTful. API Gateway mencionado.
- **Middleware IA:** Cache inteligente (similaridade via Redis/NLP/embeddings), tagging, context awareness, histórico, fallback, filas background (BullMQ).
- **Logs:** Estruturado (Pino/Winston), IDs correlação.
- **Segurança:** Helmet, CORS, rate limiting (Redis), sanitização.
- **Configuração:** `.env` por ambiente.
- **Módulos ES:** `type: "module"`.

### Testes e Qualidade
- **Ferramentas:** Jest, Supertest.
- **Cobertura:** Meta >65% (ideal >90%), relatórios (Codecov).
- **Mocks:** `jest.unstable_mockModule`.
- **CI/CD:** GitHub Actions (testes automáticos, simulação serviços). Proteção `master`.
- **Segurança Deps:** Dependabot.

### Interface e Experiência do Usuário (UI/UX)
- **Foco Neurodivergência:** Layout limpo, intuitivo, acessível.
- **Padrões Visuais:** Guia de estilo validado (inputs suaves, ícones azuis, SelectBoxes, botão Cancelar branco). Cores/contrastes acessíveis.
- **Componentes:** Modais padronizados.
- **Feedback:** Indicadores visuais, animações, reforços positivos.
- **Acessibilidade:** Modo específico planejado (ver Seção 15).

### Documentação
- **API:** Swagger (OpenAPI 3.0) automático (`@swagger`), endpoint `/api-docs`, exportação JSON, Markdown para GitHub.
- **Arquitetura:** Planejado uso de C4 e BPMN.

### Infraestrutura
- **Containerização:** Docker (app, Redis, MongoDB).
- **Monitoramento:** Planos para ElasticStack ou Loki/Grafana.
- **Healthcheck:** Endpoint `/healthcheck`.

### Observações Gerais do Projeto
- **Equipe:** 1 pessoa (GP, Dev, QA).
- **Esforço/Orçamento:** ~10h/semana por ~30 semanas (MVP), orçamento limitado.
- **Multilíngue:** pt, en.

---

## Referências

Consolidação baseada nos arquivos fornecidos em `drive-download-20250525T184532Z-1-001.zip`, incluindo análises de seções, documentos de escopo anteriores e análises específicas (Geolocalização, Diário Seguro, Integração Tarefas, Lista de Compras, Medicação como Tarefa).

