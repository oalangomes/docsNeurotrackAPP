#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Cadastro e Perfil"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'acessar_app': {
        'type': 'acao',
        'label': '🚀 Acessar app\nNeurotrack pela\nprimeira vez'
    },
    'decisao_conta': {
        'type': 'decisao',
        'label': 'Já possui\nconta?'
    },
    'preencher_email': {
        'type': 'acao',
        'label': '📝 Preencher\ne-mail e senha'
    },
    'preencher_cadastro': {
        'type': 'entrada',
        'label': '📋 Preencher dados\nde cadastro\n(nome, e-mail, senha)'
    },
    'autenticar': {
        'type': 'acao',
        'label': '✅ Autenticar\ne criar conta'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'acessar_app'),
    ('acessar_app', 'decisao_conta'),
    ('decisao_conta', 'preencher_email', 'Sim'),
    ('decisao_conta', 'preencher_cadastro', 'Não'),
    ('preencher_email', 'autenticar'),
    ('preencher_cadastro', 'autenticar'),
    ('autenticar', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'cadastro_e_perfil_improved',
    'Cadastro e Perfil do Usuário',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
