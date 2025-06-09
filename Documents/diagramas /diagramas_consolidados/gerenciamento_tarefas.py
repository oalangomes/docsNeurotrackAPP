from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.analytics import Spark
from diagrams.programming.language import Python

# Criar diagrama consolidado para Gerenciamento de Tarefas
with Diagram("Gerenciamento de Tarefas - NeurotrackApp", show=False, direction="TB", filename="gerenciamento_tarefas_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nGerenciamento de Tarefas")
    
    # Opções de gerenciamento de tarefas
    with Cluster("Opções de Gerenciamento de Tarefas"):
        criar_tarefa = Action("Criar nova\ntarefa")
        visualizar_tarefas = Action("Visualizar\nlista de tarefas")
        filtrar_tarefas = Action("Filtrar tarefas\npor status/prioridade")
    
    # Criação de tarefa
    with Cluster("Criação de Tarefa"):
        definir_titulo = InputOutput("Definir título\nda tarefa")
        adicionar_descricao = InputOutput("Adicionar descrição\n(opcional)")
        definir_prioridade = InputOutput("Definir prioridade\n(1-5)")
        adicionar_tags = InputOutput("Adicionar tags\nsensoriais")
        definir_data = InputOutput("Definir data\nde vencimento")
        adicionar_subtarefas = Action("Adicionar\nsubtarefas")
    
    # Gerenciamento de tarefas
    with Cluster("Gerenciamento de Tarefas"):
        ver_detalhes = InputOutput("Ver detalhes\nda tarefa")
        editar_tarefa = Action("Editar tarefa\nexistente")
        marcar_concluida = Action("Marcar como\nconcluída")
        excluir_tarefa = Action("Excluir tarefa")
        reordenar_tarefas = Action("Reordenar\ntarefas")
    
    # Assistência de IA
    with Cluster("Assistência de IA"):
        sugerir_decomposicao = Action("Sugerir decomposição\nde tarefas complexas")
        recomendar_prioridade = Action("Recomendar\nprioridades")
        estimar_tempo = Action("Estimar tempo\nde conclusão")
    
    # Análise de IA
    analise_ia = Spark("Análise de padrões\ncom IA")
    
    # Banco de dados
    db_tarefas = Database("Banco de Dados\nde Tarefas")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> criar_tarefa
    acessar_secao >> visualizar_tarefas
    acessar_secao >> filtrar_tarefas
    
    # Fluxo de criação
    criar_tarefa >> definir_titulo >> adicionar_descricao >> definir_prioridade >> adicionar_tags >> definir_data
    definir_data >> adicionar_subtarefas
    adicionar_subtarefas >> db_tarefas
    
    # Assistência de IA na criação
    criar_tarefa >> sugerir_decomposicao
    definir_prioridade >> recomendar_prioridade
    adicionar_subtarefas >> estimar_tempo
    
    # Fluxo de visualização e gerenciamento
    visualizar_tarefas >> ver_detalhes
    ver_detalhes >> editar_tarefa
    ver_detalhes >> marcar_concluida
    ver_detalhes >> excluir_tarefa
    visualizar_tarefas >> reordenar_tarefas
    
    # Interações com banco de dados
    editar_tarefa >> db_tarefas
    marcar_concluida >> db_tarefas
    excluir_tarefa >> db_tarefas
    reordenar_tarefas >> db_tarefas
    
    # Análise e relatórios
    filtrar_tarefas >> analise_ia
    
    # Conexões com banco de dados para análise
    db_tarefas >> analise_ia
    
    # Finalização
    analise_ia >> fim
    marcar_concluida >> fim
    excluir_tarefa >> fim
