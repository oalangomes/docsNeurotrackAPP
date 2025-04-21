#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Entrada Diária (Journaling)"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'abrir_entrada': {
        'type': 'acao',
        'label': '📝 Abrir nova\nentrada diária'
    },
    'selecionar_humor': {
        'type': 'entrada',
        'label': '😊 Selecionar humor\ndo dia'
    },
    'escrever_texto': {
        'type': 'entrada',
        'label': '✏️ Escrever texto\nlivre sobre o dia'
    },
    'decisao_sugestao': {
        'type': 'decisao',
        'label': 'Deseja sugestão\nda IA?'
    },
    'gerar_sugestao': {
        'type': 'acao',
        'label': '🤖 [Sistema:] Gerar\nsugestão baseada\nno contexto'
    },
    'salvar_entrada': {
        'type': 'acao',
        'label': '💾 Salvar entrada\nno diário'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'abrir_entrada'),
    ('abrir_entrada', 'selecionar_humor'),
    ('selecionar_humor', 'escrever_texto'),
    ('escrever_texto', 'decisao_sugestao'),
    ('decisao_sugestao', 'gerar_sugestao', 'Sim'),
    ('decisao_sugestao', 'salvar_entrada', 'Não'),
    ('gerar_sugestao', 'salvar_entrada'),
    ('salvar_entrada', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'entrada_diaria_improved',
    'Entrada Diária (Journaling)',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
