from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.aws.ml import Comprehend
from diagrams.programming.language import Python

# Criar diagrama consolidado para Preferências Avançadas
with Diagram("Preferências Avançadas - NeurotrackApp", show=False, direction="TB", filename="preferencias_avancadas_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nPreferências Avançadas")
    
    # Opções de preferências avançadas
    with Cluster("Opções de Preferências Avançadas"):
        personalizar_interface = Action("Personalizar\ninterface")
        configurar_acessibilidade = Action("Configurar opções\nde acessibilidade")
        ajustar_neurodivergencia = Action("Ajustar perfil\nneurodivergente")
    
    # Personalização de interface
    with Cluster("Personalização de Interface"):
        tema_visual = InputOutput("Selecionar tema\nvisual")
        tamanho_fonte = InputOutput("Ajustar tamanho\nde fonte")
        layout_app = InputOutput("Configurar layout\ndo aplicativo")
        organizar_modulos = Action("Organizar módulos\nna tela inicial")
    
    # Configurações de acessibilidade
    with Cluster("Configurações de Acessibilidade"):
        alto_contraste = Action("Ativar modo\nalto contraste")
        leitor_tela = Action("Configurar leitor\nde tela")
        navegacao_voz = Action("Ativar navegação\npor voz")
        simplificar_interface = Action("Simplificar\ninterface")
    
    # Ajustes para neurodivergência
    with Cluster("Ajustes para Neurodivergência"):
        perfil_tdah = Action("Configurar perfil\nTDAH")
        perfil_autismo = Action("Configurar perfil\nTEA")
        perfil_dislexia = Action("Configurar perfil\ndislexia")
        perfil_personalizado = InputOutput("Criar perfil\npersonalizado")
    
    # Configurações específicas para TDAH
    with Cluster("Configurações para TDAH"):
        lembretes_frequentes = Action("Ativar lembretes\nfrequentes")
        temporizadores_visuais = Action("Usar temporizadores\nvisuais")
        reduzir_distracao = Action("Reduzir elementos\nde distração")
    
    # Configurações específicas para TEA
    with Cluster("Configurações para TEA"):
        previsibilidade = Action("Aumentar\nprevisibilidade")
        reduzir_estimulos = Action("Reduzir estímulos\nsensoriais")
        rotinas_visuais = Action("Usar rotinas\nvisuais")
    
    # Sistema de IA para recomendações
    sistema_recomendacao = Comprehend("Sistema de\nRecomendação IA")
    
    # Banco de dados
    db_preferencias = Database("Banco de Dados\nde Preferências")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> personalizar_interface
    acessar_secao >> configurar_acessibilidade
    acessar_secao >> ajustar_neurodivergencia
    
    # Personalização de interface
    personalizar_interface >> tema_visual
    personalizar_interface >> tamanho_fonte
    personalizar_interface >> layout_app
    personalizar_interface >> organizar_modulos
    
    # Configurações de acessibilidade
    configurar_acessibilidade >> alto_contraste
    configurar_acessibilidade >> leitor_tela
    configurar_acessibilidade >> navegacao_voz
    configurar_acessibilidade >> simplificar_interface
    
    # Ajustes para neurodivergência
    ajustar_neurodivergencia >> perfil_tdah
    ajustar_neurodivergencia >> perfil_autismo
    ajustar_neurodivergencia >> perfil_dislexia
    ajustar_neurodivergencia >> perfil_personalizado
    
    # Configurações específicas para TDAH
    perfil_tdah >> lembretes_frequentes
    perfil_tdah >> temporizadores_visuais
    perfil_tdah >> reduzir_distracao
    
    # Configurações específicas para TEA
    perfil_autismo >> previsibilidade
    perfil_autismo >> reduzir_estimulos
    perfil_autismo >> rotinas_visuais
    
    # Recomendações de IA
    perfil_personalizado >> sistema_recomendacao
    sistema_recomendacao >> lembretes_frequentes
    sistema_recomendacao >> reduzir_estimulos
    
    # Interações com banco de dados
    tema_visual >> db_preferencias
    tamanho_fonte >> db_preferencias
    layout_app >> db_preferencias
    organizar_modulos >> db_preferencias
    alto_contraste >> db_preferencias
    leitor_tela >> db_preferencias
    navegacao_voz >> db_preferencias
    simplificar_interface >> db_preferencias
    perfil_tdah >> db_preferencias
    perfil_autismo >> db_preferencias
    perfil_dislexia >> db_preferencias
    perfil_personalizado >> db_preferencias
    
    # Finalização
    organizar_modulos >> fim
    simplificar_interface >> fim
    lembretes_frequentes >> fim
    rotinas_visuais >> fim
