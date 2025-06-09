# Análise Detalhada - Seção 1: Cadastro, Autenticação e Perfil do Usuário

---

## **1. Criação de Conta**

**Original:**  
Permitir cadastro utilizando e-mail e senha, com validações adequadas. Suporte também para login social via Google (OAuth).

**Comentário Técnico:**  
- Excelente definição inicial.  
- A inclusão de login social no MVP já demonstra visão de acessibilidade e praticidade para o público neurodivergente.  
- Recomendável explicitar se o e-mail é verificado (via link/token) antes do primeiro login.

**Sugestão de melhoria:**  
> Validação de e-mail com envio de token antes do primeiro login para reforçar segurança e ativação.

**História de Usuário Real:**  
*Como uma jovem adulta com TDAH, quero poder entrar rapidamente no app com meu login do Google para não perder o foco e desistir do cadastro, o que costumo fazer em apps complexos.*

---

## **2. Autenticação**

**Original:**  
Implementar login seguro utilizando JSON Web Tokens (JWT) para proteger endpoints da API.

**Comentário Técnico:**  
- Uso de JWT é adequado e alinhado com boas práticas.  
- Sugere-se avaliar o uso de refresh tokens para melhorar a experiência em sessões prolongadas.

**Sugestão de melhoria:**  
> Avaliar uso de refresh tokens com armazenamento seguro (HttpOnly) e expiração adaptativa para sessões longas.

**História de Usuário:**  
*Como um pai que acessa o app à noite para revisar o dia da filha, quero manter minha sessão ativa por mais tempo para não precisar logar novamente toda hora.*

---

## **3. Preenchimento de Perfil Complementar**

**Original:**  
Após o cadastro inicial, solicitar informações adicionais como nome, idade/data de nascimento, idioma, gênero (opcional).

**Comentário Funcional:**  
- Estrutura modular adequada.  
- O campo “gênero (opcional)” é uma boa prática inclusiva.  
- Considerar onboarding progressivo.

**História de Usuário:**  
*Como uma pessoa neurodivergente com TEA, fico ansiosa com cadastros longos. Quero preencher aos poucos para não abandonar o processo.*

---

## **4. Perfil Neurodivergente**

**Original:**  
Coletar informações sobre diagnósticos (ex: TDAH, TEA), sintomas e estágio (este último visível apenas se um diagnóstico for selecionado).

**Comentário Técnico:**  
- Excelente separação entre “diagnóstico” e “estágio”, com condicionalidade visual.  
- Recomenda-se permitir múltiplos diagnósticos e adicionar tooltips.

**História de Usuário:**  
*Como uma mãe de uma criança com TDAH e TEA, quero informar ambos os diagnósticos para que o app possa ajustar sugestões conforme o perfil duplo.*

---

## **5. Detecção Automática**

**Original:**  
Inferir automaticamente o status "Neurodivergente?" e o "Tipo de Perfil" com base nos dados fornecidos (lógica no backend).

**Comentário Técnico:**  
- Lógica inferida é excelente para evitar erros de preenchimento.  
- Testes com casos ambíguos são essenciais.

**História de Usuário:**  
*Como um adolescente em investigação diagnóstica, quero que o app me identifique como perfil potencialmente neurodivergente mesmo sem um diagnóstico fechado.*

---

## **6. Gestão de Dependentes**

**Original:**  
Permitir vincular responsáveis e dependentes (para cenários de uso por pais/responsáveis).

**Comentário Funcional:**  
- Estratégia inteligente para escalar o app para uso familiar e clínico.  
- Backend precisa lidar com permissões e múltiplos perfis.

**História de Usuário:**  
*Como pai de duas crianças neurodivergentes, quero ver o progresso de cada uma separadamente, mas também comparar rotinas e ajustes familiares.*

---

## **7. Resumo Final**

**Original:**  
Apresentar uma tela de resumo ao final do processo de cadastro/perfil.

**Comentário UX:**  
- Boa prática de usabilidade.  
- Ideal permitir edição antes de confirmar.

**História de Usuário:**  
*Como uma mãe atarefada, quero revisar se preenchi os dados dos meus filhos corretamente antes de finalizar, para não ter que refazer depois.*

---

## **8. Segurança da Conta (MVP inicial)**

**Original:**  
Incluir funcionalidades básicas como logout.

**Comentário Técnico:**  
- Logout é essencial, mas o mínimo.  
- Ideal planejar desde já exclusão de conta, recuperação de senha, etc.

**História de Usuário:**  
*Como um jovem adulto que compartilha o celular, quero sair do app facilmente para que ninguém veja meus registros pessoais.*