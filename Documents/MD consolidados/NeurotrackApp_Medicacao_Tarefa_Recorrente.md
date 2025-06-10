# Estratégia de Integração: Medicação como Tarefa Recorrente Inteligente

---

## ✅ Decisão Estratégica

Ao cadastrar uma medicação, o sistema **deve gerar automaticamente tarefas recorrentes**, mas a **gestão de adesão** deve permanecer nativa na aba de Medicações.

---

## 🎯 Justificativa

### Vantagens de transformar medicação em tarefa:
- Centraliza lembretes e notificações no módulo de tarefas.
- Permite visualização unificada do dia.
- Usa recursos existentes: prioridade, níveis de energia, status.
- Facilita análises futuras com a IA (correlação entre humor e adesão).

### Limitações:
- Tarefas e medicações têm natureza distinta.
- A conclusão de tarefa fora do horário pode comprometer o rastreamento.
- Histórico de adesão exige lógica própria (não apenas “concluído”).

---

## 🧠 Comportamento Ideal (Dupla Camada)

1. **Cadastro de Medicação**  
   → Define horários, dose, frequência.

2. **Geração de Tarefas Recorrentes (invisíveis ou visíveis)**  
   - Título: “Tomar [Nome do Remédio] – [Hora]”  
   - Tags: `medicação`, `baixa energia`  
   - Frequência: diária ou personalizada  
   - Notificação no horário

3. **Registro de Uso no Módulo de Medicação**  
   - O botão de “check” na medicação alimenta o histórico de adesão.  
   - Essa ação também marca a tarefa como concluída, se vinculada.

4. **Análise de IA (futuro)**  
   - Ex: “Risperidona às 20h + entrada no diário: 'muito sonolento às 21h'”  
   - Insight: “Possível sonolência induzida pela medicação?”

---

## 🧾 Exemplo de Tarefa Criada

- **Título:** "Tomar Risperidona – 20h"  
- **Tags:** `medicação`, `noturno`, `baixa energia`  
- **Nível de energia:** 0  
- **Repetição:** Diária às 20h  
- **Notificação:** Sim  
- **Link com adesão:** Medicação X do usuário

---

## ✅ Conclusão

A criação automática de tarefas recorrentes **aumenta a eficácia dos lembretes**, sem abrir mão do **controle específico de adesão e histórico** da aba de medicação. Essa abordagem reforça a sinergia entre os módulos e prepara o terreno para **análises inteligentes futuras**.