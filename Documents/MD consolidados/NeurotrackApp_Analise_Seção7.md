# Análise Detalhada - Seção 7: Gestão de Medicação

---

## **1. CRUD de Medicações**

**Original:**  
Permitir o cadastro, edição e exclusão de medicamentos, incluindo nome, dose, horários e frequência.

**Comentário Técnico e Funcional:**  
- Excelente escopo base.  
- Sugestão: incluir tipo, via de administração e instruções extras.  
- Aplicar autoformatação para unidade (mg, gotas, ml etc).

**História de Usuário Real:**  
*Como pai de uma criança neurodivergente com múltiplas medicações, quero registrar as doses e horários corretamente, sem confusão, para evitar erros.*

---

## **2. Lembretes**

**Original:**  
Configurar lembretes visuais e/ou notificações para a tomada de medicação.

**Comentário de UX:**  
- Essencial para adesão.  
- Deve oferecer opções de múltiplos horários, som, vibração e persistência.  
- Integração futura com assistentes de voz é um diferencial.

**História de Usuário:**  
*Como uma mulher com TDAH, frequentemente esqueço de tomar remédio. Quero que o app me avise com uma notificação clara e que fique visível até que eu confirme a tomada.*

---

## **3. Registro de Uso**

**Original:**  
Possibilitar marcar a medicação como tomada (check).

**Comentário Técnico:**  
- Importante para rastreamento.  
- Deve permitir visualização por dia e marcação com ou sem justificativa.  
- Exemplo: “não tomado - efeito colateral”.

**História de Usuário:**  
*Como um adolescente em transição para autonomia, quero marcar se tomei ou não o remédio, para eu mesmo acompanhar minha responsabilidade.*

---

## **4. Histórico e Relatórios**

**Original:**  
Visualizar histórico de adesão e, futuramente, gerar relatórios de adesão.

**Comentário Estratégico:**  
- Valioso para terapeutas e médicos.  
- Relatórios: percentual de adesão, lista por data, exportação em CSV/PDF.  
- Visual gráfico é um diferencial.

**História de Usuário:**  
*Como mãe de uma criança em tratamento, quero exportar um relatório de medicação para mostrar na consulta com o neurologista.*

---

## **5. Integração com Diário (Futuro)**

**Original:**  
Futuramente, permitir relacionar a tomada de medicação com efeitos percebidos registrados na entrada diária.

**Comentário Técnico e IA:**  
- Excelente diferencial.  
- Correlação entre timestamps pode gerar insights automatizados da IA.  
- Exemplo: sonolência após uso → IA sugere ajuste ou alerta.

**História de Usuário:**  
*Como terapeuta ocupacional, quero ver se o humor ou foco do meu paciente está sendo afetado por uma medicação específica.*