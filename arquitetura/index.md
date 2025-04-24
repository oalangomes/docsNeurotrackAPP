---
layout: default
title: Arquitetura
---

# Arquitetura do NeurotrackApp

Esta seção contém a documentação detalhada da arquitetura do NeurotrackApp, incluindo diagramas C4, descrições dos componentes e decisões de design.

## Diagramas de Arquitetura

<div class="module-grid">
  <div class="module-card">
    <h3><a href="contexto/">Diagrama de Contexto</a></h3>
    <p>Visão geral do sistema e suas integrações externas.</p>
    <a href="contexto/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="containers/">Diagrama de Containers</a></h3>
    <p>Representação dos principais contêineres do sistema.</p>
    <a href="containers/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="componentes-backend/">Componentes do Backend</a></h3>
    <p>Detalhamento dos componentes do backend.</p>
    <a href="componentes-backend/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="componentes-frontend/">Componentes do Frontend</a></h3>
    <p>Estrutura detalhada da aplicação frontend.</p>
    <a href="componentes-frontend/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="codigo/">Diagrama de Código</a></h3>
    <p>Detalhamento dos módulos principais de código.</p>
    <a href="codigo/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="fluxo-dados/">Fluxo de Dados</a></h3>
    <p>Visualização de como os dados fluem através do sistema.</p>
    <a href="fluxo-dados/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="seguranca-autenticacao/">Segurança e Autenticação</a></h3>
    <p>Mecanismos de segurança em todas as camadas do sistema.</p>
    <a href="seguranca-autenticacao/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="implantacao-infraestrutura/">Implantação e Infraestrutura</a></h3>
    <p>Detalhamento da infraestrutura de hospedagem.</p>
    <a href="implantacao-infraestrutura/" class="btn">Ver detalhes</a>
  </div>
  
  <div class="module-card">
    <h3><a href="integracao-servicos/">Integração com Serviços Externos</a></h3>
    <p>Conexões com APIs e serviços de terceiros.</p>
    <a href="integracao-servicos/" class="btn">Ver detalhes</a>
  </div>
</div>

## Visão Geral da Arquitetura

O NeurotrackApp utiliza uma arquitetura de microsserviços, com separação clara entre frontend e backend. O backend é construído em Node.js, utilizando Express para a API RESTful, MongoDB para persistência de dados e integração com serviços externos como OpenAI para funcionalidades de IA e Google Calendar para agenda.

## Análise de Lacunas

Esta seção também inclui uma análise das lacunas identificadas na arquitetura atual e recomendações para melhorias futuras.
