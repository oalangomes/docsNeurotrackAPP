#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Análises e Relatórios"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'visualizar_graficos': {
        'type': 'acao',
        'label': '📊 Visualizar gráficos\n(humor, tarefas, etc.)'
    },
    'decisao_exportar': {
        'type': 'decisao',
        'label': 'Deseja exportar\nos dados?'
    },
    'gerar_arquivo': {
        'type': 'acao',
        'label': '📁 Gerar PDF\nou CSV'
    },
    'voltar_visualizacao': {
        'type': 'acao',
        'label': '🔍 Voltar para\nvisualização'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'visualizar_graficos'),
    ('visualizar_graficos', 'decisao_exportar'),
    ('decisao_exportar', 'gerar_arquivo', 'Sim'),
    ('decisao_exportar', 'voltar_visualizacao', 'Não'),
    ('gerar_arquivo', 'fim'),
    ('voltar_visualizacao', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'analises_e_relatorios_improved',
    'Análises e Relatórios',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
