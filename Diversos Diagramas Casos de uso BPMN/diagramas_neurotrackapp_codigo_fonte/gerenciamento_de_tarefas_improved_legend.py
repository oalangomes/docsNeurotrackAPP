#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Gerenciamento de Tarefas"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'criar_tarefa': {
        'type': 'acao',
        'label': '📋 Criar nova tarefa\n(com prioridade,\ncategoria, status)'
    },
    'decisao_subtarefas': {
        'type': 'decisao',
        'label': 'Deseja dividir\nem subtarefas?'
    },
    'preencher_subtarefas': {
        'type': 'entrada',
        'label': '📑 Preencher\nsubtarefas'
    },
    'marcar_concluida': {
        'type': 'acao',
        'label': '✅ Marcar tarefa\ncomo concluída'
    },
    'visualizar_filtrar': {
        'type': 'acao',
        'label': '🔍 Visualizar e\nfiltrar tarefas'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'criar_tarefa'),
    ('criar_tarefa', 'decisao_subtarefas'),
    ('decisao_subtarefas', 'preencher_subtarefas', 'Sim'),
    ('decisao_subtarefas', 'marcar_concluida', 'Não'),
    ('preencher_subtarefas', 'marcar_concluida'),
    ('marcar_concluida', 'visualizar_filtrar'),
    ('visualizar_filtrar', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'gerenciamento_de_tarefas_improved',
    'Gerenciamento de Tarefas',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
