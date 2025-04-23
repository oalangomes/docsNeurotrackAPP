---
layout: default
title: Documentação da API
---

# Documentação da API do NeurotrackApp

Esta seção contém a documentação detalhada da API do NeurotrackApp, incluindo endpoints, modelos de dados, parâmetros de requisição e exemplos de resposta.

## Endpoints da API

<div class="module-grid">
  <div class="module-card">
    <h3><a href="autenticacao/">Autenticação e Usuários</a></h3>
    <p>Endpoints para login, registro e gerenciamento de perfil.</p>
    <a href="autenticacao/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="entradas-diarias/">Entradas Diárias</a></h3>
    <p>Endpoints para registro e consulta de entradas diárias.</p>
    <a href="entradas-diarias/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="tarefas/">Tarefas</a></h3>
    <p>Endpoints para gerenciamento de tarefas e subtarefas.</p>
    <a href="tarefas/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="ia/">Inteligência Artificial</a></h3>
    <p>Endpoints para interação com IA e análise de dados.</p>
    <a href="ia/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="medicacao/">Medicação</a></h3>
    <p>Endpoints para gerenciamento de medicamentos.</p>
    <a href="medicacao/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="agenda/">Agenda</a></h3>
    <p>Endpoints para gerenciamento de eventos e integração com Google Calendar.</p>
    <a href="agenda/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="health/">Monitoramento de Saúde</a></h3>
    <p>Endpoints para verificação de status da API.</p>
    <a href="health/" class="btn">Ver detalhes</a>
  </div>
</div>

## Swagger

A documentação completa da API está disponível no formato Swagger/OpenAPI, permitindo testes interativos e visualização detalhada de todos os endpoints.

<div class="cta-container">
  <a href="swagger/" class="btn btn-large">Acessar Documentação Swagger</a>
</div>

## Modelos de Dados

Esta seção inclui a definição detalhada de todos os modelos de dados utilizados pela API:

- User
- DailyEntry
- Task
- Medication
- Event
- AIAnalysis
- Settings

## Autenticação

A API do NeurotrackApp utiliza autenticação JWT (JSON Web Token). Todos os endpoints, exceto login e registro, requerem um token válido no cabeçalho de autorização.

```
Authorization: Bearer <token>
```

## Exemplos de Uso

Exemplos práticos de como utilizar cada endpoint da API, incluindo requisições e respostas.
