#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Integração com Agenda"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'criar_evento': {
        'type': 'acao',
        'label': '📅 Criar evento\nlocal'
    },
    'decisao_sincronizar': {
        'type': 'decisao',
        'label': 'Deseja sincronizar\ncom Google\nCalendar?'
    },
    'autenticar_oauth': {
        'type': 'entrada',
        'label': '🔑 Autenticar\nvia OAuth'
    },
    'receber_lembretes': {
        'type': 'acao',
        'label': '⏰ Receber\nlembretes'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'criar_evento'),
    ('criar_evento', 'decisao_sincronizar'),
    ('decisao_sincronizar', 'autenticar_oauth', 'Sim'),
    ('decisao_sincronizar', 'receber_lembretes', 'Não'),
    ('autenticar_oauth', 'receber_lembretes'),
    ('receber_lembretes', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'integracao_com_agenda_improved',
    'Integração com Agenda',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
