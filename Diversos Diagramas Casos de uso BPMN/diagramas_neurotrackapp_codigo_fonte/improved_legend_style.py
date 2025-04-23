#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import graphviz
import os
from PIL import Image, ImageDraw, ImageFont

def create_bpmn_diagram(filename, title, nodes, connections):
    """
    Cria um diagrama BPMN com estilo compacto e legenda no canto inferior direito,
    exatamente como no exemplo fornecido.
    
    Args:
        filename: Nome do arquivo para salvar o diagrama
        title: Título do diagrama
        nodes: Dicionário de nós com seus tipos e rótulos
        connections: Lista de conexões entre nós
    """
    # Configuração do diagrama
    dot = graphviz.Digraph(filename, 
                          comment=f'Diagrama BPMN - {title} (NeurotrackApp)',
                          format='png')
    
    # Configurações gerais do diagrama para layout mais compacto
    dot.attr(rankdir='TB', 
             size='7,10!', 
             dpi='300',
             fontname='Arial',
             nodesep='0.3',
             ranksep='0.5')
    
    # Definição de estilos compactos
    dot.attr('node', fontname='Arial', fontsize='11', margin='0.1')
    dot.attr('edge', fontname='Arial', fontsize='10', arrowsize='0.7')
    
    # Adicionar nós ao diagrama
    for node_id, node_info in nodes.items():
        node_type = node_info['type']
        label = node_info['label']
        
        if node_type == 'inicio' or node_type == 'fim':
            # Círculos verdes para início e fim
            dot.node(node_id, label, shape='circle', style='filled', 
                    fillcolor='#4CAF50', fontcolor='white', 
                    width='0.8', height='0.8', penwidth='0')
        
        elif node_type == 'acao':
            # Retângulos azuis para ações comuns
            dot.node(node_id, label, shape='box', style='filled,rounded', 
                    fillcolor='#2196F3', fontcolor='white', 
                    width='2.0', height='0.7', penwidth='0')
        
        elif node_type == 'entrada':
            # Retângulos laranja para etapas de entrada personalizada
            dot.node(node_id, label, shape='box', style='filled,rounded', 
                    fillcolor='#FF9800', fontcolor='white', 
                    width='2.0', height='0.7', penwidth='0')
        
        elif node_type == 'decisao':
            # Losangos pretos para decisões
            dot.node(node_id, label, shape='diamond', style='filled', 
                    fillcolor='#1E1E1E', fontcolor='white', 
                    width='1.2', height='1.2', penwidth='0')
    
    # Adicionar conexões
    for conn in connections:
        if len(conn) == 2:
            # Conexão simples
            dot.edge(conn[0], conn[1])
        elif len(conn) == 3:
            # Conexão com rótulo
            dot.edge(conn[0], conn[1], label=conn[2])
    
    # Título do diagrama no topo (sem título no rodapé)
    dot.attr(labelloc='t')  # Posicionar o título no topo
    dot.attr(label=f'{title} - NeurotrackApp', fontsize='16', fontname='Arial Bold')
    
    # Renderizar o diagrama principal
    dot.render(directory='/home/ubuntu/neurotrackapp_diagramas', view=False)
    
    # Criar legenda personalizada usando PIL
    create_custom_legend(f'/home/ubuntu/neurotrackapp_diagramas/{filename}.gv.png', 
                         f'/home/ubuntu/neurotrackapp_diagramas/{filename}_final.png')
    
    return f'/home/ubuntu/neurotrackapp_diagramas/{filename}_final.png'

def create_custom_legend(input_path, output_path):
    """
    Cria uma legenda personalizada exatamente como no exemplo e a adiciona à imagem.
    
    Args:
        input_path: Caminho da imagem do diagrama
        output_path: Caminho para salvar a imagem final com legenda
    """
    # Abrir a imagem do diagrama
    img = Image.open(input_path)
    width, height = img.size
    
    # Definir cores
    green_color = (76, 175, 80)  # #4CAF50
    blue_color = (33, 150, 243)  # #2196F3
    orange_color = (255, 152, 0)  # #FF9800
    black_color = (30, 30, 30)   # #1E1E1E
    
    # Criar a legenda com tamanho maior
    legend_width = 400  # Aumentado
    legend_height = 250  # Aumentado
    legend = Image.new('RGBA', (legend_width, legend_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(legend)
    
    # Desenhar o fundo da legenda com bordas arredondadas
    # Primeiro um retângulo branco com borda cinza claro
    draw.rounded_rectangle(
        [(0, 0), (legend_width-1, legend_height-1)],
        radius=20,
        fill=(255, 255, 255, 230),
        outline=(220, 220, 220)
    )
    
    # Adicionar título da legenda
    try:
        font_title = ImageFont.truetype("Arial Bold", 18)  # Aumentado
        font_text = ImageFont.truetype("Arial", 16)  # Aumentado
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
    
    draw.text((legend_width//2, 25), "Legenda", fill=(0, 0, 0), font=font_title, anchor="mm")
    
    # Desenhar os ícones e textos da legenda
    y_start = 70  # Aumentado
    y_spacing = 45  # Aumentado
    
    # Início/Fim
    circle_size = 20  # Aumentado
    draw.ellipse([(30, y_start-circle_size), (30+circle_size*2, y_start+circle_size)], fill=green_color)
    draw.text((90, y_start), "Início", fill=(0, 0, 0), font=font_text, anchor="lm")
    
    # Etapas de ação comum
    y_start += y_spacing
    box_size = 20  # Aumentado
    draw.rounded_rectangle([(30, y_start-box_size), (30+box_size*2, y_start+box_size)], radius=5, fill=blue_color)
    draw.text((90, y_start), "Etapas de ação comum", fill=(0, 0, 0), font=font_text, anchor="lm")
    
    # Etapas com entrada personalizada
    y_start += y_spacing
    draw.rounded_rectangle([(30, y_start-box_size), (30+box_size*2, y_start+box_size)], radius=5, fill=orange_color)
    draw.text((90, y_start), "Etapas com entrada", fill=(0, 0, 0), font=font_text, anchor="lm")
    draw.text((90, y_start+25), "personalizada", fill=(0, 0, 0), font=font_text, anchor="lm")
    
    # Decisão
    y_start += y_spacing + 25
    # Desenhar um losango
    diamond_size = 20  # Aumentado
    diamond_points = [
        (30+diamond_size, y_start-diamond_size),  # topo
        (30+diamond_size*2, y_start),     # direita
        (30+diamond_size, y_start+diamond_size),  # base
        (30, y_start),     # esquerda
    ]
    draw.polygon(diamond_points, fill=black_color)
    draw.text((90, y_start), "Decisão", fill=(0, 0, 0), font=font_text, anchor="lm")
    
    # Posicionar a legenda no canto inferior direito
    position = (width - legend_width - 20, height - legend_height - 20)
    
    # Combinar a imagem do diagrama com a legenda
    img.paste(legend, position, legend)
    
    # Salvar a imagem final
    img.save(output_path)
