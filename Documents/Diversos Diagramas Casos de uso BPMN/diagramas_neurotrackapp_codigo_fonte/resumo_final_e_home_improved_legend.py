#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Resumo Final e Home"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'exibir_entradas': {
        'type': 'acao',
        'label': '📝 Exibir entradas\ndo dia'
    },
    'exibir_tarefas': {
        'type': 'acao',
        'label': '📋 Exibir tarefas\ndo dia'
    },
    'exibir_respostas': {
        'type': 'acao',
        'label': '💬 Exibir respostas\nrecentes da IA'
    },
    'mostrar_recomendacoes': {
        'type': 'acao',
        'label': '🌟 Mostrar recomendações\ndiárias personalizadas'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'exibir_entradas'),
    ('exibir_entradas', 'exibir_tarefas'),
    ('exibir_tarefas', 'exibir_respostas'),
    ('exibir_respostas', 'mostrar_recomendacoes'),
    ('mostrar_recomendacoes', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'resumo_final_e_home_improved',
    'Resumo Final e Home',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
