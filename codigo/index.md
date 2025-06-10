---
layout: default
title: Código e Implementação
---

# Código e Implementação do NeurotrackApp

Esta seção contém a documentação detalhada do código-fonte do NeurotrackApp, incluindo estrutura de diretórios, principais módulos e guias de implementação.

## Estrutura do Projeto

<div class="module-grid">
  <div class="module-card">
    <h3><a href="backend/">Backend (Node.js)</a></h3>
    <p>Implementação em Node.js com Express, seguindo arquitetura de microsserviços.</p>
    <a href="backend/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="frontend/">Frontend (React Native)</a></h3>
    <p>Interface multiplataforma desenvolvida em React Native.</p>
    <a href="frontend/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="banco-dados/">Banco de Dados</a></h3>
    <p>Estrutura do MongoDB e modelos de dados.</p>
    <a href="banco-dados/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="integracoes/">Integrações</a></h3>
    <p>Implementação das integrações com serviços externos.</p>
    <a href="integracoes/" class="btn">Ver detalhes</a>
  </div>
</div>

## Backend

O backend do NeurotrackApp é implementado em Node.js com Express, seguindo uma arquitetura de microsserviços. Os principais módulos incluem:

- **Autenticação**: Implementação de login, registro e gerenciamento de sessões com JWT
- **Entradas Diárias**: Registro e análise de humor e atividades diárias
- **Tarefas**: Gerenciamento de tarefas e subtarefas
- **IA**: Integração com OpenAI para análise de padrões e recomendações
- **Medicação**: Controle de medicamentos e lembretes
- **Agenda**: Integração com Google Calendar e gerenciamento de eventos

## Frontend

O frontend do NeurotrackApp está em desenvolvimento utilizando React Native para suporte multiplataforma (iOS e Android). A interface é projetada com foco em acessibilidade e usabilidade para pessoas neurodivergentes.

## Análise de Inconsistências

Esta seção inclui uma análise das inconsistências identificadas entre o código, a documentação e o Swagger, com recomendações para alinhamento.

<div class="cta-container">
  <a href="inconsistencias/" class="btn btn-large">Ver Análise de Inconsistências</a>
</div>
