# Preferências Avançadas

O módulo de Preferências Avançadas do NeurotrackApp permite uma personalização profunda da experiência do usuário, com foco especial nas necessidades específicas de pessoas neurodivergentes, oferecendo ajustes de interface, acessibilidade e comportamento do aplicativo.

## Diagrama de Fluxo

![Preferências Avançadas](../assets/images/preferencias_avancadas_consolidado.png)

## Principais Funcionalidades

### Personalização de Interface
- **Seleção de tema visual**: Escolha entre temas claros, escuros ou personalizados
- **Ajuste de tamanho de fonte**: Configuração para melhor legibilidade
- **Configuração de layout**: Organização dos elementos na tela
- **Organização de módulos**: Priorização de funcionalidades mais utilizadas
- **Densidade de informação**: Ajuste da quantidade de informações exibidas simultaneamente

### Configurações de Acessibilidade
- **Modo alto contraste**: Melhor visualização para pessoas com deficiência visual
- **Compatibilidade com leitor de tela**: Suporte a tecnologias assistivas
- **Navegação por voz**: Controle do aplicativo através de comandos de voz
- **Simplificação de interface**: Redução de elementos visuais para minimizar sobrecarga
- **Ajustes de animações**: Controle ou desativação de efeitos visuais

### Perfis Neurodivergentes
- **TDAH**: Configurações específicas para Transtorno do Déficit de Atenção e Hiperatividade
- **TEA**: Ajustes para Transtorno do Espectro Autista
- **Dislexia**: Adaptações para facilitar a leitura
- **Perfil personalizado**: Combinação de configurações conforme necessidades individuais

### Configurações Específicas por Perfil
- **TDAH**: Lembretes frequentes, temporizadores visuais, redução de distrações
- **TEA**: Previsibilidade, redução de estímulos, rotinas visuais
- **Dislexia**: Fontes específicas, espaçamento de texto, guias de leitura

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /users/preferences | Obtenção das preferências do usuário |
| PUT | /users/preferences/interface | Atualização de preferências de interface |
| PUT | /users/preferences/accessibility | Atualização de configurações de acessibilidade |
| PUT | /users/preferences/neuro-profile | Atualização de perfil neurodivergente |
| GET | /users/preferences/templates | Obtenção de modelos de configuração predefinidos |

## Cenários de Uso

### Configuração de Perfil para TDAH
1. Usuário acessa a seção de Preferências Avançadas
2. Seleciona a opção de perfil neurodivergente
3. Escolhe o perfil "TDAH" entre as opções disponíveis
4. Sistema aplica configurações predefinidas para TDAH:
   - Lembretes mais frequentes para tarefas
   - Interface com menos elementos distrativos
   - Temporizadores visuais para atividades
   - Decomposição automática de tarefas
5. Usuário pode ajustar individualmente cada configuração
6. Salva as preferências e recebe confirmação

### Personalização de Interface Visual
1. Usuário acessa configurações de interface
2. Seleciona tema visual (claro, escuro ou personalizado)
3. Ajusta tamanho de fonte para melhor legibilidade
4. Configura densidade de informação nas telas
5. Reorganiza módulos na tela inicial conforme frequência de uso
6. Visualiza prévia das alterações em tempo real
7. Confirma as mudanças e aplica ao aplicativo

### Configuração para Usuário com TEA
1. Usuário com TEA acessa preferências avançadas
2. Seleciona perfil TEA ou cria perfil personalizado
3. Ativa opções de previsibilidade (avisos antes de mudanças)
4. Configura redução de estímulos visuais e sonoros
5. Ativa rotinas visuais para tarefas recorrentes
6. Ajusta comunicações para serem mais diretas e literais
7. Sistema aplica as configurações em todos os módulos do aplicativo
