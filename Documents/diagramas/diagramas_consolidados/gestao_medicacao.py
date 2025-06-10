from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.monitoring import Grafana
from diagrams.programming.language import Python

# Criar diagrama consolidado para Gestão de Medicação
with Diagram("Gestão de Medicação - NeurotrackApp", show=False, direction="TB", filename="gestao_medicacao_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nGestão de Medicação")
    
    # Opções de gestão de medicação
    with Cluster("Opções de Gestão de Medicação"):
        adicionar_medicacao = Action("Adicionar nova\nmedicação")
        visualizar_medicacoes = Action("Visualizar lista\nde medicações")
        ver_historico = Action("Ver histórico\nde aderência")
    
    # Adição de medicação
    with Cluster("Adição de Medicação"):
        nome_medicacao = InputOutput("Informar nome\nda medicação")
        dosagem = InputOutput("Definir dosagem")
        frequencia = InputOutput("Definir frequência\n(diária, semanal)")
        horarios = InputOutput("Definir horários\nde administração")
        duracao = InputOutput("Definir duração\ndo tratamento")
        observacoes = InputOutput("Adicionar\nobservações")
    
    # Gerenciamento de medicações
    with Cluster("Gerenciamento de Medicações"):
        ver_detalhes = InputOutput("Ver detalhes\nda medicação")
        editar_medicacao = Action("Editar medicação\nexistente")
        excluir_medicacao = Action("Excluir medicação")
        marcar_tomada = Action("Marcar medicação\ncomo tomada")
        configurar_lembretes = Action("Configurar\nlembretes")
    
    # Monitoramento e relatórios
    with Cluster("Monitoramento e Relatórios"):
        verificar_aderencia = InputOutput("Verificar taxa\nde aderência")
        gerar_relatorio = Action("Gerar relatório\nde medicação")
        compartilhar_relatorio = Action("Compartilhar com\nprofissional de saúde")
    
    # Lembretes e notificações
    sistema_lembretes = Grafana("Sistema de\nLembretes")
    
    # Banco de dados
    db_medicacoes = Database("Banco de Dados\nde Medicações")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> adicionar_medicacao
    acessar_secao >> visualizar_medicacoes
    acessar_secao >> ver_historico
    
    # Fluxo de adição
    adicionar_medicacao >> nome_medicacao >> dosagem >> frequencia >> horarios >> duracao >> observacoes
    observacoes >> db_medicacoes
    
    # Configuração de lembretes
    horarios >> configurar_lembretes
    configurar_lembretes >> sistema_lembretes
    
    # Fluxo de visualização e gerenciamento
    visualizar_medicacoes >> ver_detalhes
    ver_detalhes >> editar_medicacao
    ver_detalhes >> excluir_medicacao
    ver_detalhes >> marcar_tomada
    
    # Interações com banco de dados
    editar_medicacao >> db_medicacoes
    excluir_medicacao >> db_medicacoes
    marcar_tomada >> db_medicacoes
    
    # Monitoramento e relatórios
    ver_historico >> verificar_aderencia
    verificar_aderencia >> gerar_relatorio
    gerar_relatorio >> compartilhar_relatorio
    
    # Conexões com banco de dados para relatórios
    db_medicacoes >> verificar_aderencia
    
    # Sistema de lembretes
    sistema_lembretes >> usuario
    
    # Finalização
    compartilhar_relatorio >> fim
    marcar_tomada >> fim
    excluir_medicacao >> fim
