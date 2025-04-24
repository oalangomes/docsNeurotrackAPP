#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from improved_legend_style import create_bpmn_diagram

# Definição dos nós para o diagrama "Chat IA Personalizado"
nodes = {
    'inicio': {
        'type': 'inicio',
        'label': 'Início'
    },
    'abrir_chat': {
        'type': 'acao',
        'label': '💬 Abrir chat'
    },
    'enviar_pergunta': {
        'type': 'entrada',
        'label': '❓ Enviar pergunta\nou desabafo'
    },
    'buscar_sugestao': {
        'type': 'acao',
        'label': '🤖 [Sistema:] Buscar\nsugestão no cache\nou gerar nova'
    },
    'mostrar_resposta': {
        'type': 'acao',
        'label': '📱 Mostrar resposta\nda IA'
    },
    'decisao_salvar': {
        'type': 'decisao',
        'label': 'Deseja salvar\nsugestão como\nentrada?'
    },
    'salvar_sugestao': {
        'type': 'acao',
        'label': '💾 Salvar sugestão\ncomo entrada'
    },
    'fim': {
        'type': 'fim',
        'label': 'Fim'
    }
}

# Definição das conexões entre os nós
connections = [
    ('inicio', 'abrir_chat'),
    ('abrir_chat', 'enviar_pergunta'),
    ('enviar_pergunta', 'buscar_sugestao'),
    ('buscar_sugestao', 'mostrar_resposta'),
    ('mostrar_resposta', 'decisao_salvar'),
    ('decisao_salvar', 'salvar_sugestao', 'Sim'),
    ('decisao_salvar', 'fim', 'Não'),
    ('salvar_sugestao', 'fim')
]

# Criar o diagrama
diagram_path = create_bpmn_diagram(
    'chat_ia_personalizado_improved',
    'Chat IA Personalizado',
    nodes,
    connections
)

print(f"Diagrama criado com sucesso: {diagram_path}")
