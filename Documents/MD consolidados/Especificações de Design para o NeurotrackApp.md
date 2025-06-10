# Especificações de Design para o NeurotrackApp

## Visão Geral

Este documento apresenta especificações detalhadas de design para o NeurotrackApp, com foco em melhorias para usuários neurodivergentes. As especificações são baseadas na análise das telas originais do aplicativo e incluem recomendações para implementação de tema escuro, redesenho de telas prioritárias e novas funcionalidades complementares.

## Paleta de Cores

### Tema Claro (Existente)
- **Fundo principal**: #FFFFFF (branco)
- **Fundo de cards**: #F5F7FA (cinza muito claro)
- **Texto principal**: #212121 (quase preto)
- **Texto secundário**: #757575 (cinza médio)
- **Cor primária**: #4285F4 (azul Google)
- **Cor de sucesso**: #34A853 (verde)
- **Cor de alerta**: #FBBC05 (amarelo)
- **Cor de erro**: #EA4335 (vermelho)

### Tema Escuro (Novo)
- **Fundo principal**: #121212 (preto suave)
- **Fundo de cards**: #2D2D2D (cinza escuro)
- **Texto principal**: #FFFFFF (branco)
- **Texto secundário**: #B3B3B3 (cinza claro)
- **Cor primária**: #8AB4F8 (azul claro)
- **Cor de sucesso**: #81C995 (verde claro)
- **Cor de alerta**: #FDD663 (amarelo claro)
- **Cor de erro**: #F28B82 (vermelho claro)

## Tipografia

- **Fonte principal**: Roboto ou San Francisco (dependendo da plataforma)
- **Tamanhos de texto**:
  - Títulos principais: 24sp
  - Subtítulos: 18sp
  - Texto de corpo: 16sp
  - Texto secundário: 14sp
  - Rótulos pequenos: 12sp

## Elementos de Interface

### Cards
- **Cantos arredondados**: 12dp de raio
- **Elevação**: 1dp (tema claro), 4dp (tema escuro)
- **Espaçamento interno**: 16dp em todos os lados
- **Espaçamento entre cards**: 12dp

### Botões
- **Botões primários**:
  - Fundo: cor primária
  - Texto: branco
  - Cantos arredondados: 24dp
  - Altura: 48dp
  - Padding horizontal: 24dp

- **Botões secundários**:
  - Contorno: 1dp cor primária
  - Texto: cor primária
  - Fundo: transparente
  - Mesmas dimensões dos botões primários

### Campos de Entrada
- **Altura**: 56dp
- **Cantos arredondados**: 8dp
- **Padding horizontal**: 16dp
- **Rótulos**: Posicionados acima do campo, 12sp
- **Texto de entrada**: 16sp
- **Ícones**: Alinhados à esquerda, 24dp x 24dp

### Ícones
- **Tamanho padrão**: 24dp x 24dp
- **Ícones de navegação**: 20dp x 20dp
- **Ícones de ação**: 24dp x 24dp
- **Cor**: Cor primária ou texto secundário

## Especificações por Tela

### 1. Tela de Termos de Uso

#### Versão Atual
- Design minimalista com título centralizado
- Ícone de documento centralizado
- Texto explicativo centralizado
- Checkbox para aceitação
- Botões de "Cancelar" e "Continuar" na parte inferior

#### Melhorias Recomendadas
- **Tema Escuro**: Implementar versão com fundo escuro e texto claro
- **Acessibilidade**:
  - Adicionar versão simplificada dos termos em formato de tópicos
  - Incluir opção para baixar os termos completos em PDF
  - Implementar indicador de progresso para documentos longos
  - Destacar termos importantes com formatação diferenciada
- **Interatividade**:
  - Feedback visual mais claro ao marcar o checkbox
  - Botão "Continuar" desabilitado até que os termos sejam aceitos

### 2. Tela de Perfil e Preferências

#### Versão Atual
- Cards separados para diferentes categorias de informações
- Ícones à esquerda para cada categoria
- Botões de edição (ícone de lápis) à direita
- Informações organizadas em linhas dentro de cada card

#### Melhorias Recomendadas
- **Tema Escuro**: Implementar versão com fundo escuro e texto claro
- **Acessibilidade**:
  - Aumentar contraste entre elementos
  - Adicionar rótulos descritivos para ícones
  - Implementar feedback tátil ao tocar nos botões de edição
- **Organização**:
  - Adicionar indicadores visuais de prioridade para informações críticas
  - Implementar sistema de abas para facilitar a navegação entre categorias
  - Adicionar botão de "Voltar ao topo" para telas longas

### 3. Tela de Edição de Medicação

#### Versão Atual
- Campos para nome do medicamento, dosagem e horários
- Botão para adicionar horários adicionais
- Botão para adicionar outro medicamento
- Botões de "Cancelar" e "Salvar alterações" na parte inferior

#### Melhorias Recomendadas
- **Tema Escuro**: Implementar versão com fundo escuro e texto claro
- **Acessibilidade**:
  - Adicionar seletor de horário mais intuitivo com feedback visual
  - Implementar sugestões automáticas para nomes de medicamentos comuns
  - Adicionar campo para notas ou instruções especiais
- **Funcionalidade**:
  - Implementar sistema de lembretes personalizáveis
  - Adicionar opção para definir estoque e alertas de reabastecimento
  - Incluir histórico de medicação tomada/pulada

### 4. Tela de Edição de Produtividade

#### Versão Atual
- Campos para horários de pico, duração ideal de tarefa e duração máxima contínua
- Interface simples com ícones representativos
- Botões de "Cancelar" e "Salvar alterações" na parte inferior

#### Melhorias Recomendadas
- **Tema Escuro**: Implementar versão com fundo escuro e texto claro
- **Acessibilidade**:
  - Adicionar visualização gráfica dos horários de pico
  - Implementar seletores de tempo mais intuitivos
  - Incluir explicações contextuais sobre cada configuração
- **Funcionalidade**:
  - Adicionar opção para definir intervalos entre tarefas
  - Implementar sugestões baseadas em padrões de produtividade
  - Incluir opção para dias diferentes da semana

### 5. Tela de Edição de Diagnóstico

#### Versão Atual
- Seleção de diagnósticos (TEA, TDAH, TAB) com chips
- Campo para seleção de estágio
- Botões de "Cancelar" e "Salvar alterações" na parte inferior

#### Melhorias Recomendadas
- **Tema Escuro**: Implementar versão com fundo escuro e texto claro
- **Acessibilidade**:
  - Adicionar descrições breves para cada diagnóstico
  - Implementar seleção de múltiplos diagnósticos com feedback visual claro
  - Incluir opção para adicionar notas específicas sobre cada diagnóstico
- **Funcionalidade**:
  - Adicionar recursos educacionais relacionados aos diagnósticos selecionados
  - Implementar recomendações personalizadas baseadas nos diagnósticos
  - Incluir opção para registrar profissionais de saúde associados

## Novas Telas Complementares

### 1. Dashboard/Home

#### Especificações
- **Cabeçalho**:
  - Saudação personalizada com nome do usuário
  - Data atual
  - Ícone de configurações no canto superior direito
- **Resumo do Dia**:
  - Card com progresso diário (barra de progresso visual)
  - Próximas atividades com horários
  - Medicações pendentes com alertas visuais
- **Estatísticas da Semana**:
  - Cards pequenos com estatísticas-chave (tarefas, medicação, humor)
  - Indicadores visuais de tendência (melhorando/piorando)
- **Acesso Rápido**:
  - Botões para funções frequentes (adicionar tarefa, registrar medicação, etc.)
  - Atalho para assistente virtual (BuddyBot)
- **Navegação**:
  - Barra inferior com ícones para telas principais

### 2. Assistente Virtual (BuddyBot)

#### Especificações
- **Cabeçalho**:
  - Título "BuddyBot"
  - Botão de voltar no canto superior esquerdo
- **Interface de Chat**:
  - Bolhas de mensagem com diferenciação visual entre usuário e assistente
  - Ícone do BuddyBot para mensagens do assistente
  - Área de entrada de texto na parte inferior
  - Botão de envio à direita da área de entrada
- **Funcionalidades**:
  - Respostas rápidas sugeridas (botões clicáveis)
  - Capacidade de mostrar lembretes de medicação
  - Análise de humor e progresso
  - Lembretes de consultas e compromissos
- **Acessibilidade**:
  - Opção de entrada por voz
  - Respostas em texto e áudio
  - Ajuste de velocidade de resposta

## Recomendações Gerais de Implementação

### Transições e Animações
- Usar animações sutis para transições entre telas (duração: 300ms)
- Implementar feedback visual imediato para ações do usuário
- Permitir desabilitar animações nas configurações de acessibilidade

### Feedback Tátil e Sonoro
- Vibração sutil ao pressionar botões (opcional, configurável)
- Sons discretos para confirmações e alertas (opcional, configurável)
- Feedback visual alternativo para usuários que desabilitam feedback tátil/sonoro

### Modo de Alto Contraste
- Versão alternativa do tema escuro com contraste ainda maior
- Bordas mais definidas entre elementos
- Texto com tamanho aumentado

### Suporte a Gestos
- Implementar gestos intuitivos (deslizar para voltar, etc.)
- Fornecer alternativas baseadas em botões para todas as ações por gestos
- Tutorial visual para gestos disponíveis

### Personalização
- Permitir reordenação de elementos na tela inicial
- Opções para ocultar ou destacar funcionalidades específicas
- Perfis pré-configurados para diferentes condições neurodivergentes

## Considerações Técnicas

### Responsividade
- Design adaptável a diferentes tamanhos de tela
- Breakpoints para smartphones pequenos, médios e grandes
- Suporte a orientação retrato e paisagem

### Performance
- Otimização para carregamento rápido (< 2 segundos)
- Armazenamento local de dados frequentemente acessados
- Sincronização eficiente com backend

### Acessibilidade
- Compatibilidade com leitores de tela (TalkBack/VoiceOver)
- Suporte a navegação por teclado
- Conformidade com WCAG 2.1 AA

## Conclusão

Estas especificações de design fornecem diretrizes detalhadas para a implementação de melhorias no NeurotrackApp, com foco especial nas necessidades de usuários neurodivergentes. A implementação destas recomendações resultará em uma experiência de usuário mais acessível, intuitiva e eficaz, mantendo a identidade visual e funcional do aplicativo original enquanto incorpora melhorias significativas de usabilidade e acessibilidade.
