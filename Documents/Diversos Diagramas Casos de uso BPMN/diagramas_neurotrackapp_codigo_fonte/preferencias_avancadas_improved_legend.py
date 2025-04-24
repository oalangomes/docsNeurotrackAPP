#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Preferências Avançadas"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'escolher_linguagem': {
        'type': 'entrada',
        'label': '💬 Escolher estilo de\nlinguagem da IA'
    },
    'selecionar_temas': {
        'type': 'entrada',
        'label': '🔍 Selecionar temas\nde interesse'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'escolher_linguagem'),
    ('escolher_linguagem', 'selecionar_temas'),
    ('selecionar_temas', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'preferencias_avancadas_improved',
    'Preferências Avançadas',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
