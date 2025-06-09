# Especificações do Tema Escuro para o NeurotrackApp

## Visão Geral

Este documento apresenta especificações detalhadas para a implementação do tema escuro (Dark Mode) no NeurotrackApp, com foco especial nas necessidades de usuários neurodivergentes. O tema escuro não é apenas uma preferência estética, mas uma necessidade de acessibilidade para muitos usuários com sensibilidade visual, incluindo pessoas com TDAH, TEA e outras condições neurodivergentes.

## Paleta de Cores do Tema Escuro

### Cores Primárias
- **Fundo principal**: #121212 (preto suave)
- **Fundo de cards**: #2D2D2D (cinza escuro)
- **Fundo de campos de entrada**: #383838 (cinza médio-escuro)
- **Fundo de barras e cabeçalhos**: #1F1F1F (preto acinzentado)

### Cores de Texto
- **Texto principal**: #FFFFFF (branco)
- **Texto secundário**: #B3B3B3 (cinza claro)
- **Texto desabilitado**: #757575 (cinza médio)
- **Texto em campos de entrada**: #E0E0E0 (cinza muito claro)

### Cores de Ação
- **Cor primária**: #8AB4F8 (azul claro)
- **Cor primária pressionada**: #4285F4 (azul Google)
- **Cor de sucesso**: #81C995 (verde claro)
- **Cor de alerta**: #FDD663 (amarelo claro)
- **Cor de erro**: #F28B82 (vermelho claro)

### Cores de Estado
- **Selecionado**: #3C4043 (cinza escuro) com borda #8AB4F8 (azul claro)
- **Hover**: #3C4043 (cinza escuro)
- **Ripple effect**: #8AB4F8 com 20% de opacidade

### Gradientes
- **Gradiente primário**: Linear de #8AB4F8 a #4285F4
- **Gradiente de sucesso**: Linear de #81C995 a #34A853
- **Gradiente de alerta**: Linear de #FDD663 a #FBBC05

## Princípios de Design para o Tema Escuro

### 1. Contraste e Legibilidade
- Manter proporção de contraste mínima de 4.5:1 entre texto e fundo
- Usar texto branco (#FFFFFF) apenas em fundos suficientemente escuros
- Evitar texto cinza em fundos cinza sem diferença significativa de luminosidade
- Aumentar o peso da fonte em 1 nível para textos pequenos

### 2. Hierarquia Visual
- Usar variações sutis de cinza para criar profundidade
- Aplicar elevação através de sombras suaves (com opacidade reduzida)
- Manter consistência na hierarquia de informações entre temas claro e escuro
- Usar cor primária (#8AB4F8) para destacar elementos importantes

### 3. Feedback Visual
- Aumentar a visibilidade dos estados de hover e foco
- Implementar efeitos de ripple mais visíveis para feedback tátil
- Usar animações sutis para transições entre estados
- Fornecer feedback visual imediato para todas as interações

### 4. Redução de Fadiga Visual
- Evitar grandes áreas de branco puro
- Reduzir o brilho geral da interface
- Minimizar o uso de cores saturadas em grandes áreas
- Implementar transições suaves entre telas

## Especificações por Elemento de Interface

### Cards
- **Fundo**: #2D2D2D
- **Borda**: Nenhuma (usar elevação em vez de bordas)
- **Elevação**: Sombra com 10% de opacidade, 4dp de deslocamento
- **Cantos arredondados**: 12dp
- **Espaçamento interno**: 16dp em todos os lados

### Botões
- **Botão primário**:
  - Fundo: #8AB4F8 (azul claro)
  - Texto: #121212 (preto suave)
  - Estado pressionado: #4285F4 (azul Google)
  - Elevação: 2dp

- **Botão secundário**:
  - Fundo: Transparente
  - Borda: 1dp #8AB4F8 (azul claro)
  - Texto: #8AB4F8 (azul claro)
  - Estado pressionado: #8AB4F8 com 20% de opacidade

- **Botão terciário/texto**:
  - Fundo: Transparente
  - Texto: #8AB4F8 (azul claro)
  - Estado pressionado: #8AB4F8 com 10% de opacidade

### Campos de Entrada
- **Fundo**: #383838 (cinza médio-escuro)
- **Borda em repouso**: 1dp #5F6368 (cinza)
- **Borda em foco**: 2dp #8AB4F8 (azul claro)
- **Texto de entrada**: #E0E0E0 (cinza muito claro)
- **Texto de placeholder**: #757575 (cinza médio)
- **Rótulo**: #B3B3B3 (cinza claro)

### Switches e Toggles
- **Track desativado**: #5F6368 (cinza)
- **Track ativado**: #8AB4F8 com 50% de opacidade
- **Thumb desativado**: #BDBDBD (cinza claro)
- **Thumb ativado**: #8AB4F8 (azul claro)

### Barras de Progresso
- **Track**: #5F6368 (cinza)
- **Indicador**: #8AB4F8 (azul claro)
- **Indicador de sucesso**: #81C995 (verde claro)
- **Indicador de alerta**: #FDD663 (amarelo claro)

### Ícones
- **Ícones primários**: #FFFFFF (branco)
- **Ícones secundários**: #B3B3B3 (cinza claro)
- **Ícones interativos**: #8AB4F8 (azul claro)
- **Ícones desabilitados**: #757575 (cinza médio)

## Especificações por Tela

### 1. Tela de Termos de Uso (Tema Escuro)

- **Fundo principal**: #121212
- **Card de conteúdo**: #2D2D2D
- **Título "Termos de Uso"**: #FFFFFF, 24sp, centralizado
- **Ícone de documento**: #8AB4F8, 48dp x 48dp, centralizado
- **Texto explicativo**: #B3B3B3, 16sp, centralizado
- **Checkbox**: 
  - Não selecionado: Contorno #B3B3B3
  - Selecionado: Preenchimento #8AB4F8, ícone de check #121212
- **Texto do checkbox**: #FFFFFF, 16sp
- **Botão "Cancelar"**: 
  - Fundo: Transparente
  - Borda: 1dp #8AB4F8
  - Texto: #8AB4F8, 16sp
- **Botão "Continuar"**: 
  - Fundo: #8AB4F8
  - Texto: #121212, 16sp, negrito

### 2. Tela de Perfil e Preferências (Tema Escuro)

- **Fundo principal**: #121212
- **Cards de categorias**: #2D2D2D
- **Títulos de seção**: #FFFFFF, 18sp, negrito
- **Ícones de categoria**: #8AB4F8, 24dp x 24dp
- **Informações do usuário**: #FFFFFF, 16sp
- **Informações secundárias**: #B3B3B3, 14sp
- **Ícones de edição (lápis)**: #8AB4F8, 20dp x 20dp
- **Separadores entre seções**: #383838, 1dp de espessura
- **Indicadores de navegação (>)**: #757575, 16dp x 16dp

### 3. Tela de Edição de Medicação (Tema Escuro)

- **Fundo principal**: #121212
- **Cabeçalho "Editar medicação"**: #FFFFFF, 24sp, negrito
- **Ícone de fechar (X)**: #FFFFFF, 24dp x 24dp
- **Rótulos de campo**: #B3B3B3, 14sp
- **Ícones de campo**:
  - Medicamento: #8AB4F8, 24dp x 24dp
  - Dosagem: #8AB4F8, 24dp x 24dp
  - Horários: #8AB4F8, 24dp x 24dp
- **Campos de entrada**:
  - Fundo: #383838
  - Texto: #FFFFFF, 16sp
- **Horários configurados**:
  - Fundo: #383838
  - Texto: #FFFFFF, 16sp
- **Botão "+ Adicionar horário"**:
  - Texto: #8AB4F8, 14sp
  - Ícone +: #8AB4F8, 16dp x 16dp
- **Botão "+ Adicionar outro medicamento"**:
  - Fundo: Transparente
  - Borda: 1dp #8AB4F8
  - Texto: #8AB4F8, 16sp
  - Ícone +: #8AB4F8, 16dp x 16dp
- **Botões de ação**:
  - "Cancelar": Igual ao padrão de botão secundário
  - "Salvar alterações": Igual ao padrão de botão primário

### 4. Tela de Edição de Produtividade (Tema Escuro)

- **Fundo principal**: #121212
- **Cabeçalho "Editar produtividade"**: #FFFFFF, 24sp, negrito
- **Rótulos de seção**:
  - "Horários de pico": #FFFFFF, 18sp
  - "Duração ideal de tarefa": #FFFFFF, 18sp
  - "Duração máxima contínua": #FFFFFF, 18sp
- **Ícones de seção**:
  - Relógio: #8AB4F8, 24dp x 24dp
  - Tarefa: #8AB4F8, 24dp x 24dp
- **Campos de entrada**:
  - Fundo: #383838
  - Texto: #FFFFFF, 16sp
- **Botões de ação**:
  - "Cancelar": Igual ao padrão de botão secundário
  - "Salvar alterações": Igual ao padrão de botão primário

### 5. Tela de Edição de Diagnóstico (Tema Escuro)

- **Fundo principal**: #121212
- **Cabeçalho "Editar Diagnóstico"**: #FFFFFF, 24sp, negrito
- **Rótulo "Diagnósticos"**: #FFFFFF, 18sp
- **Chips de diagnóstico**:
  - Não selecionado: Fundo #383838, Texto #B3B3B3
  - Selecionado: Fundo #8AB4F8 com 30% de opacidade, Texto #FFFFFF, Borda 1dp #8AB4F8
- **Ícone de diagnóstico**: #8AB4F8, 24dp x 24dp
- **Rótulo "Estágio"**: #FFFFFF, 18sp
- **Campo de seleção de estágio**:
  - Fundo: #383838
  - Texto: #FFFFFF, 16sp
  - Ícone de seta: #B3B3B3, 16dp x 16dp
- **Botões de ação**:
  - "Cancelar": Igual ao padrão de botão secundário
  - "Salvar alterações": Igual ao padrão de botão primário

## Novas Telas Complementares (Tema Escuro)

### 1. Dashboard/Home (Tema Escuro)

- **Fundo principal**: #121212
- **Barra superior**:
  - Fundo: #1F1F1F
  - Título "NeuroTrack": #FFFFFF, 18sp, negrito
  - Ícone de menu: #FFFFFF, 24dp x 24dp
- **Saudação**:
  - "Olá, [Nome]!": #FFFFFF, 24sp, negrito
  - Data atual: #B3B3B3, 14sp
- **Card de resumo do dia**:
  - Fundo: #2D2D2D
  - Título "Resumo do dia": #FFFFFF, 16sp, negrito
  - Barra de progresso: Track #5F6368, Indicador #8AB4F8
  - Texto de progresso: #FFFFFF, 14sp
  - Valor de progresso: #8AB4F8, 18sp, negrito
- **Cards de próximas atividades**:
  - Fundo: #2D2D2D
  - Título "Próximas atividades": #FFFFFF, 16sp, negrito
  - Nome da atividade: #FFFFFF, 14sp
  - Horário: #FDD663 (para próximas), #B3B3B3 (para futuras), 14sp
  - Ícones: #8AB4F8, 20dp x 20dp
- **Cards de estatísticas**:
  - Fundo: Cor temática com 10% de opacidade
  - Nome da estatística: #FFFFFF, 12sp
  - Valor: Cor temática, 16sp, negrito
  - Cores temáticas:
    - Tarefas: #8AB4F8 (azul claro)
    - Medicação: #81C995 (verde claro)
    - Humor: #FDD663 (amarelo claro)
- **Card do BuddyBot**:
  - Fundo: #8AB4F8 com 10% de opacidade
  - Ícone do bot: #8AB4F8, 32dp x 32dp
  - Texto principal: #FFFFFF, 14sp
  - Texto secundário: #8AB4F8, 12sp
- **Barra de navegação inferior**:
  - Fundo: #1F1F1F
  - Ícones não selecionados: #B3B3B3, 24dp x 24dp
  - Ícone selecionado: #8AB4F8, 24dp x 24dp

### 2. Assistente Virtual BuddyBot (Tema Escuro)

- **Fundo principal**: #121212
- **Barra superior**:
  - Fundo: #1F1F1F
  - Título "BuddyBot": #FFFFFF, 18sp, negrito
  - Botão de voltar: #FFFFFF, 24dp x 24dp
- **Área de chat**:
  - Fundo: #121212
- **Bolhas de mensagem do bot**:
  - Fundo: #2D2D2D
  - Texto: #FFFFFF, 14sp
  - Ícone do bot: #8AB4F8, 24dp x 24dp
- **Bolhas de mensagem do usuário**:
  - Fundo: #8AB4F8 com 20% de opacidade
  - Texto: #FFFFFF, 14sp
- **Área de entrada de texto**:
  - Fundo: #383838
  - Placeholder: #757575, 14sp
  - Texto de entrada: #FFFFFF, 14sp
  - Botão de envio: #8AB4F8, 32dp x 32dp
- **Botões de resposta rápida**:
  - Fundo: Transparente
  - Borda: 1dp #8AB4F8
  - Texto: #8AB4F8, 12sp

## Transição entre Temas

### Detecção e Configuração
- Detectar automaticamente a preferência do sistema (modo claro/escuro)
- Permitir substituição manual nas configurações do aplicativo
- Opção para programar a mudança automática baseada no horário

### Animação de Transição
- Duração da transição: 300ms
- Curva de animação: Ease-in-out
- Transição simultânea de todos os elementos
- Opção para desabilitar a animação de transição

### Persistência
- Salvar a preferência de tema do usuário
- Manter a consistência do tema em todas as telas
- Aplicar o tema escolhido em todas as sessões futuras

## Considerações de Acessibilidade para o Tema Escuro

### Sensibilidade Visual
- Evitar contrastes extremos que possam causar desconforto
- Implementar opção de ajuste de brilho dentro do tema escuro
- Oferecer variação "Extra escuro" para usuários com alta sensibilidade

### Daltonismo
- Garantir que todas as informações transmitidas por cor também sejam comunicadas por forma ou texto
- Testar o tema escuro com simulações de diferentes tipos de daltonismo
- Usar combinações de cores seguras para todos os tipos de daltonismo

### Epilepsia Fotossensível
- Evitar completamente flashes ou alternâncias rápidas de contraste
- Limitar animações a movimentos suaves e graduais
- Permitir desabilitar todas as animações

### Fadiga Cognitiva
- Reduzir a quantidade de informações apresentadas simultaneamente
- Usar agrupamento visual claro para reduzir a carga cognitiva
- Implementar modo "Foco" com ainda menos elementos visuais

## Implementação Técnica

### CSS/Styles
```css
/* Exemplo de variáveis CSS para tema escuro */
:root {
  --dark-background: #121212;
  --dark-surface: #2D2D2D;
  --dark-input-background: #383838;
  --dark-primary: #8AB4F8;
  --dark-on-primary: #121212;
  --dark-on-background: #FFFFFF;
  --dark-on-surface: #FFFFFF;
  --dark-on-surface-medium: #B3B3B3;
  --dark-on-surface-disabled: #757575;
  --dark-success: #81C995;
  --dark-warning: #FDD663;
  --dark-error: #F28B82;
  --dark-divider: #383838;
  --dark-elevation-1: 0px 2px 4px rgba(0, 0, 0, 0.2);
  --dark-elevation-2: 0px 4px 8px rgba(0, 0, 0, 0.4);
}

.dark-theme {
  background-color: var(--dark-background);
  color: var(--dark-on-background);
}

.dark-theme .card {
  background-color: var(--dark-surface);
  box-shadow: var(--dark-elevation-1);
}

.dark-theme .button-primary {
  background-color: var(--dark-primary);
  color: var(--dark-on-primary);
}

.dark-theme .input-field {
  background-color: var(--dark-input-background);
  color: var(--dark-on-surface);
  border: 1px solid var(--dark-divider);
}

.dark-theme .input-field:focus {
  border: 2px solid var(--dark-primary);
}
```

### Detecção de Preferência
```javascript
// Exemplo de código para detectar preferência de tema
function detectPreferredTheme() {
  // Verificar configuração do usuário no armazenamento local
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    return savedTheme;
  }
  
  // Verificar preferência do sistema
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    return 'dark';
  }
  
  // Padrão para tema claro
  return 'light';
}

// Aplicar tema
function applyTheme(theme) {
  if (theme === 'dark') {
    document.body.classList.add('dark-theme');
    document.body.classList.remove('light-theme');
  } else {
    document.body.classList.add('light-theme');
    document.body.classList.remove('dark-theme');
  }
  
  // Salvar preferência
  localStorage.setItem('theme', theme);
}

// Inicializar tema
const theme = detectPreferredTheme();
applyTheme(theme);

// Ouvir mudanças na preferência do sistema
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  const newTheme = e.matches ? 'dark' : 'light';
  // Só aplicar se o usuário não tiver uma preferência salva
  if (!localStorage.getItem('theme')) {
    applyTheme(newTheme);
  }
});
```

## Testes e Validação

### Testes de Contraste
- Verificar todas as combinações de texto/fundo com ferramentas de contraste
- Garantir que todos os elementos interativos atendam ao nível AA das WCAG
- Testar com diferentes configurações de brilho de tela

### Testes com Usuários
- Realizar testes com usuários neurodivergentes
- Coletar feedback específico sobre conforto visual e fadiga
- Ajustar com base no feedback antes da implementação final

### Testes em Diferentes Dispositivos
- Verificar a renderização em diferentes tamanhos de tela
- Testar em dispositivos com diferentes qualidades de tela (LCD, OLED, etc.)
- Garantir consistência visual em todas as plataformas

## Conclusão

Estas especificações detalhadas para o tema escuro do NeurotrackApp fornecem diretrizes abrangentes para implementação, com foco especial nas necessidades de usuários neurodivergentes. A implementação cuidadosa deste tema escuro resultará em uma experiência significativamente melhorada para usuários com sensibilidade visual, reduzindo a fadiga ocular e melhorando a acessibilidade geral do aplicativo.

O tema escuro não é apenas uma alternativa estética, mas uma característica essencial de acessibilidade que deve ser implementada com o mesmo cuidado e atenção aos detalhes que o tema claro principal.
