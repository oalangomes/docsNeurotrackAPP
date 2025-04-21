#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Gestão de Medicação"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'adicionar_medicamento': {
        'type': 'entrada',
        'label': '💊 Adicionar medicamento\ncom frequência/horário'
    },
    'gerar_lembrete': {
        'type': 'acao',
        'label': '⏰ [Sistema:] Gerar\nlembrete'
    },
    'decisao_tomado': {
        'type': 'decisao',
        'label': 'Remédio foi\ntomado?'
    },
    'marcar_tomado': {
        'type': 'acao',
        'label': '✅ Marcar como\ntomado'
    },
    'reagendar': {
        'type': 'acao',
        'label': '🔄 Reagendar ou\nnotificar'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'adicionar_medicamento'),
    ('adicionar_medicamento', 'gerar_lembrete'),
    ('gerar_lembrete', 'decisao_tomado'),
    ('decisao_tomado', 'marcar_tomado', 'Sim'),
    ('decisao_tomado', 'reagendar', 'Não'),
    ('marcar_tomado', 'fim'),
    ('reagendar', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'gestao_de_medicacao_improved',
    'Gestão de Medicação',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
