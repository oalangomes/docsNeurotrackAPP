from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.analytics import Spark, Tableau
from diagrams.aws.ml import Comprehend
from diagrams.programming.language import Python

# Criar diagrama consolidado para Análises e Relatórios
with Diagram("Análises e Relatórios - NeurotrackApp", show=False, direction="TB", filename="analises_relatorios_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nAnálises e Relatórios")
    
    # Opções de análises e relatórios
    with Cluster("Opções de Análises e Relatórios"):
        dashboard_principal = Action("Visualizar\ndashboard principal")
        relatorios_especificos = Action("Acessar relatórios\nespecíficos")
        analises_personalizadas = Action("Criar análises\npersonalizadas")
    
    # Dashboard principal
    with Cluster("Dashboard Principal"):
        resumo_humor = InputOutput("Resumo de\nhumor")
        progresso_tarefas = InputOutput("Progresso de\ntarefas")
        aderencia_medicacao = InputOutput("Aderência à\nmedicação")
        calendario_eventos = InputOutput("Calendário de\neventos")
        insights_ia = InputOutput("Insights\nda IA")
    
    # Relatórios específicos
    with Cluster("Relatórios Específicos"):
        relatorio_humor = Action("Relatório de\nhumor")
        relatorio_tarefas = Action("Relatório de\ntarefas")
        relatorio_medicacao = Action("Relatório de\nmedicação")
        relatorio_agenda = Action("Relatório de\nagenda")
    
    # Análises personalizadas
    with Cluster("Análises Personalizadas"):
        selecionar_periodo = InputOutput("Selecionar período\nde análise")
        selecionar_metricas = InputOutput("Selecionar métricas\npara análise")
        selecionar_visualizacao = InputOutput("Escolher tipo de\nvisualização")
        gerar_analise = Action("Gerar análise\npersonalizada")
    
    # Exportação e compartilhamento
    with Cluster("Exportação e Compartilhamento"):
        exportar_pdf = Action("Exportar como\nPDF")
        exportar_csv = Action("Exportar dados\nbrutos (CSV)")
        compartilhar_email = Action("Compartilhar via\ne-mail")
        compartilhar_profissional = Action("Compartilhar com\nprofissional de saúde")
    
    # Componentes de análise
    motor_analise = Spark("Motor de\nAnálise de Dados")
    visualizacao = Tableau("Sistema de\nVisualização")
    processador_ia = Comprehend("Processador de\nInsights IA")
    
    # Bancos de dados
    db_entradas = Database("Banco de Dados\nde Entradas Diárias")
    db_tarefas = Database("Banco de Dados\nde Tarefas")
    db_medicacoes = Database("Banco de Dados\nde Medicações")
    db_eventos = Database("Banco de Dados\nde Eventos")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> dashboard_principal
    acessar_secao >> relatorios_especificos
    acessar_secao >> analises_personalizadas
    
    # Dashboard principal
    dashboard_principal >> resumo_humor
    dashboard_principal >> progresso_tarefas
    dashboard_principal >> aderencia_medicacao
    dashboard_principal >> calendario_eventos
    dashboard_principal >> insights_ia
    
    # Relatórios específicos
    relatorios_especificos >> relatorio_humor
    relatorios_especificos >> relatorio_tarefas
    relatorios_especificos >> relatorio_medicacao
    relatorios_especificos >> relatorio_agenda
    
    # Análises personalizadas
    analises_personalizadas >> selecionar_periodo >> selecionar_metricas >> selecionar_visualizacao >> gerar_analise
    
    # Conexões com componentes de análise
    relatorio_humor >> motor_analise
    relatorio_tarefas >> motor_analise
    relatorio_medicacao >> motor_analise
    relatorio_agenda >> motor_analise
    gerar_analise >> motor_analise
    
    motor_analise >> visualizacao
    motor_analise >> processador_ia
    processador_ia >> insights_ia
    
    # Conexões com bancos de dados
    db_entradas >> motor_analise
    db_tarefas >> motor_analise
    db_medicacoes >> motor_analise
    db_eventos >> motor_analise
    
    # Exportação e compartilhamento
    visualizacao >> exportar_pdf
    visualizacao >> exportar_csv
    visualizacao >> compartilhar_email
    visualizacao >> compartilhar_profissional
    
    # Finalização
    exportar_pdf >> fim
    exportar_csv >> fim
    compartilhar_email >> fim
    compartilhar_profissional >> fim
