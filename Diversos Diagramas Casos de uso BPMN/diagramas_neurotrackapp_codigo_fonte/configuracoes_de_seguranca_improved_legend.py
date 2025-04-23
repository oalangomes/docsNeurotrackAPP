#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Configurações de Segurança e Conta"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'alterar_senha': {
        'type': 'entrada',
        'label': '🔑 Alterar senha'
    },
    'atualizar_email': {
        'type': 'entrada',
        'label': '📧 Atualizar e-mail'
    },
    'deletar_conta': {
        'type': 'entrada',
        'label': '❌ Deletar conta\ncom confirmação'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'alterar_senha'),
    ('alterar_senha', 'atualizar_email'),
    ('atualizar_email', 'deletar_conta'),
    ('deletar_conta', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'configuracoes_de_seguranca_improved',
    'Configurações de Segurança e Conta',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
