from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.analytics import Spark
from diagrams.programming.language import Python

# Criar diagrama consolidado para Entradas Diárias
with Diagram("Entradas Diárias - NeurotrackApp", show=False, direction="TB", filename="entradas_diarias_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nEntradas Diárias")
    
    # Opções de entradas diárias
    with Cluster("Opções de Entradas Diárias"):
        criar_entrada = Action("Criar nova\nentrada diária")
        visualizar_entradas = Action("Visualizar\nentradas anteriores")
        filtrar_entradas = Action("Filtrar entradas\npor período")
    
    # Criação de entrada diária
    with Cluster("Criação de Entrada Diária"):
        selecionar_data = InputOutput("Selecionar data")
        registrar_humor = InputOutput("Registrar nível\nde humor (1-5)")
        adicionar_texto = InputOutput("Adicionar texto\nda entrada")
        adicionar_tags = InputOutput("Adicionar tags\n(opcional)")
        anexar_midia = InputOutput("Anexar mídia\n(opcional)")
    
    # Visualização e análise
    with Cluster("Visualização e Análise"):
        ver_detalhes = InputOutput("Ver detalhes\nda entrada")
        editar_entrada = Action("Editar entrada\nexistente")
        excluir_entrada = Action("Excluir entrada")
        ver_estatisticas = InputOutput("Ver estatísticas\ne tendências")
        gerar_relatorio = Action("Gerar relatório\nde humor")
    
    # Análise de IA
    analise_ia = Spark("Análise de padrões\ncom IA")
    
    # Banco de dados
    db_entradas = Database("Banco de Dados\nde Entradas")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> criar_entrada
    acessar_secao >> visualizar_entradas
    acessar_secao >> filtrar_entradas
    
    # Fluxo de criação
    criar_entrada >> selecionar_data >> registrar_humor >> adicionar_texto >> adicionar_tags >> anexar_midia
    anexar_midia >> db_entradas
    
    # Fluxo de visualização
    visualizar_entradas >> ver_detalhes
    ver_detalhes >> editar_entrada
    ver_detalhes >> excluir_entrada
    
    # Interações com banco de dados
    editar_entrada >> db_entradas
    excluir_entrada >> db_entradas
    
    # Análise e relatórios
    filtrar_entradas >> ver_estatisticas
    ver_estatisticas >> analise_ia
    analise_ia >> gerar_relatorio
    
    # Conexões com banco de dados para análise
    db_entradas >> analise_ia
    
    # Finalização
    gerar_relatorio >> fim
    anexar_midia >> fim
    editar_entrada >> fim
    excluir_entrada >> fim
