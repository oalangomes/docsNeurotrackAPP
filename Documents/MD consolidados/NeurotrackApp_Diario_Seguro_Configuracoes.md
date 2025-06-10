# Aprimoramento do Módulo de Entrada Diária - Diário Pessoal Seguro

---

## 1. Inclusão de “Situação” nas Entradas

### Descrição:
Permitir ao usuário categorizar o contexto emocional da entrada com uma *Situação*, como:
- Reflexão pessoal
- Situação de risco
- Pensamento intrusivo
- Crise emocional
- Desabafo comum
- Relato positivo

### Impacto:
- Melhora a análise contextual da IA
- Permite atuação sensível e segura
- Ajuda o próprio usuário a nomear seu estado emocional

**História de Usuário Real:**  
*Como um jovem que lida com pensamentos agressivos, quero poder marcar meu relato como uma situação de risco para que a IA me acolha com mais cuidado e registre sem julgamento.*

---

## 2. Criptografia + Proteção por Senha ou Biometria

### Descrição:
Cada entrada pode ser:
- Criptografada localmente ou no backend
- Protegida por senha pessoal (diferente da senha de login) ou biometria

### Modos possíveis:
- Entrada pública (padrão)
- Entrada protegida (acesso por senha)
- Entrada sensível (não indexada pela IA)

**Mensagem sugerida:**  
“Este registro foi marcado como confidencial. Apenas você poderá acessá-lo, com senha ou biometria.”

**História de Usuário:**  
*Como uma adolescente que escreve sobre traumas, quero garantir que ninguém, nem por acidente, acesse esses registros mesmo que tenha meu celular desbloqueado.*

---

## 3. Análise Restrita com Foco em Risco (Autorização explícita)

### Descrição:
IA só analisa entradas protegidas se:
- O usuário autorizar no momento do registro
- A análise for restrita a detecção de risco (ideação suicida, agressividade, explosões emocionais)

### Exemplo de resposta da IA:
“Percebi que este relato pode conter uma situação difícil. Você gostaria de conversar ou receber uma sugestão acolhedora?”

**História de Usuário:**  
*Como uma mãe que está no limite emocional, quero escrever livremente sem que a IA interprete tudo, apenas intervenha com cuidado se detectar que estou em risco.*

---

## 4. Regras Técnicas Futuras

- `exportable`: false se confidencial
- `private`: true para registros protegidos
- `allowAI`: false por padrão em registros sensíveis
- `riskAnalyzed`: false até que o usuário autorize
- Flags podem ser armazenadas por entrada no backend para total controle do usuário

---

## Conclusão

Este aprimoramento transforma o diário do NeurotrackApp em um espaço verdadeiramente seguro, íntimo e respeitoso com o estado emocional dos usuários neurodivergentes.