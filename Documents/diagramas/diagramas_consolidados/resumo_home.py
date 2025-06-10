from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.analytics import Spark
from diagrams.aws.ml import Comprehend
from diagrams.programming.language import Python

# Criar diagrama consolidado para Resumo e Home
with Diagram("Resumo e Home - NeurotrackApp", show=False, direction="TB", filename="resumo_home_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    autenticar = Action("Autenticar\nusuário")
    
    # Tela inicial (Home)
    with Cluster("Tela Inicial (Home)"):
        dashboard_resumo = InputOutput("Dashboard de\nresumo")
        menu_navegacao = Action("Menu de\nnavegação")
        notificacoes = Action("Centro de\nnotificações")
        acesso_rapido = Action("Acesso rápido\naos módulos")
    
    # Componentes do Dashboard
    with Cluster("Componentes do Dashboard"):
        resumo_humor = InputOutput("Resumo de\nhumor recente")
        proximas_tarefas = InputOutput("Próximas tarefas\npendentes")
        lembretes_medicacao = InputOutput("Lembretes de\nmedicação")
        proximos_eventos = InputOutput("Próximos eventos\nda agenda")
        insights_diarios = InputOutput("Insights\ndiários")
    
    # Navegação principal
    with Cluster("Navegação Principal"):
        nav_entradas = Action("Acessar\nEntradas Diárias")
        nav_tarefas = Action("Acessar\nGerenciamento de Tarefas")
        nav_medicacao = Action("Acessar\nGestão de Medicação")
        nav_agenda = Action("Acessar\nAgenda")
        nav_ia = Action("Acessar\nAssistente IA")
        nav_relatorios = Action("Acessar\nAnálises e Relatórios")
        nav_configuracoes = Action("Acessar\nConfigurações")
    
    # Personalização da Home
    with Cluster("Personalização da Home"):
        reordenar_widgets = Action("Reordenar\nwidgets")
        ocultar_widgets = Action("Ocultar/mostrar\nwidgets")
        ajustar_tamanho = Action("Ajustar tamanho\ndos widgets")
        definir_padrao = Action("Definir layout\npadrão")
    
    # Componentes de IA
    sistema_recomendacao = Comprehend("Sistema de\nRecomendação IA")
    
    # Bancos de dados
    db_usuario = Database("Banco de Dados\nde Usuário")
    db_preferencias = Database("Banco de Dados\nde Preferências")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> autenticar >> dashboard_resumo
    
    # Componentes da tela inicial
    dashboard_resumo >> menu_navegacao
    dashboard_resumo >> notificacoes
    dashboard_resumo >> acesso_rapido
    
    # Componentes do dashboard
    dashboard_resumo >> resumo_humor
    dashboard_resumo >> proximas_tarefas
    dashboard_resumo >> lembretes_medicacao
    dashboard_resumo >> proximos_eventos
    dashboard_resumo >> insights_diarios
    
    # Navegação principal
    menu_navegacao >> nav_entradas
    menu_navegacao >> nav_tarefas
    menu_navegacao >> nav_medicacao
    menu_navegacao >> nav_agenda
    menu_navegacao >> nav_ia
    menu_navegacao >> nav_relatorios
    menu_navegacao >> nav_configuracoes
    
    # Personalização da Home
    dashboard_resumo >> reordenar_widgets
    dashboard_resumo >> ocultar_widgets
    dashboard_resumo >> ajustar_tamanho
    dashboard_resumo >> definir_padrao
    
    # Interações com IA
    insights_diarios << sistema_recomendacao
    sistema_recomendacao >> acesso_rapido
    
    # Interações com bancos de dados
    autenticar >> db_usuario
    db_usuario >> dashboard_resumo
    reordenar_widgets >> db_preferencias
    ocultar_widgets >> db_preferencias
    ajustar_tamanho >> db_preferencias
    definir_padrao >> db_preferencias
    
    # Finalização
    nav_entradas >> fim
    nav_tarefas >> fim
    nav_medicacao >> fim
    nav_agenda >> fim
    nav_ia >> fim
    nav_relatorios >> fim
    nav_configuracoes >> fim
