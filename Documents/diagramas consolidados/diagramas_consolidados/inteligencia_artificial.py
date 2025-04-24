from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.analytics import Spark
from diagrams.aws.ml import Comprehend, Rekognition
from diagrams.programming.language import Python

# Criar diagrama consolidado para Inteligência Artificial
with Diagram("Inteligência Artificial - NeurotrackApp", show=False, direction="TB", filename="inteligencia_artificial_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nAssistente IA")
    
    # Opções de interação com IA
    with Cluster("Opções de Interação com IA"):
        chat_ia = Action("Iniciar chat\ncom IA")
        solicitar_analise = Action("Solicitar análise\nde dados")
        ver_historico = Action("Ver histórico\nde interações")
    
    # Interação com chat IA
    with Cluster("Chat com IA"):
        enviar_prompt = InputOutput("Enviar prompt\nou pergunta")
        contexto_conversa = InputOutput("Fornecer contexto\n(opcional)")
        receber_resposta = InputOutput("Receber resposta\nda IA")
        avaliar_resposta = Action("Avaliar resposta\n(feedback)")
    
    # Análise de dados
    with Cluster("Análise de Dados"):
        selecionar_dados = InputOutput("Selecionar dados\npara análise")
        escolher_tipo_analise = Decision("Escolher tipo\nde análise")
        analise_humor = Action("Análise de\npadrões de humor")
        analise_tarefas = Action("Análise de\ndesempenho em tarefas")
        analise_medicacao = Action("Análise de\naderência à medicação")
        receber_insights = InputOutput("Receber insights\ne recomendações")
    
    # Personalização
    with Cluster("Personalização da IA"):
        ajustar_estilo = Action("Ajustar estilo\nde comunicação")
        definir_preferencias = Action("Definir preferências\nde interação")
        treinar_modelo = Action("Treinar modelo\ncom feedback")
    
    # Componentes de IA
    modelo_ia = Comprehend("Modelo de\nProcessamento de Linguagem")
    analise_dados = Spark("Análise de\nDados")
    
    # Banco de dados
    db_interacoes = Database("Banco de Dados\nde Interações")
    db_usuario = Database("Banco de Dados\nde Perfil do Usuário")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> chat_ia
    acessar_secao >> solicitar_analise
    acessar_secao >> ver_historico
    
    # Fluxo de chat
    chat_ia >> enviar_prompt
    enviar_prompt >> contexto_conversa >> modelo_ia
    modelo_ia >> receber_resposta
    receber_resposta >> avaliar_resposta
    
    # Fluxo de análise
    solicitar_analise >> selecionar_dados >> escolher_tipo_analise
    escolher_tipo_analise >> analise_humor
    escolher_tipo_analise >> analise_tarefas
    escolher_tipo_analise >> analise_medicacao
    analise_humor >> analise_dados
    analise_tarefas >> analise_dados
    analise_medicacao >> analise_dados
    analise_dados >> receber_insights
    
    # Personalização
    acessar_secao >> ajustar_estilo
    acessar_secao >> definir_preferencias
    avaliar_resposta >> treinar_modelo
    
    # Interações com banco de dados
    enviar_prompt >> db_interacoes
    avaliar_resposta >> db_interacoes
    receber_insights >> db_interacoes
    ajustar_estilo >> db_usuario
    definir_preferencias >> db_usuario
    treinar_modelo >> modelo_ia
    
    # Conexões com banco de dados para análise
    db_interacoes >> analise_dados
    db_usuario >> modelo_ia
    
    # Finalização
    receber_resposta >> fim
    receber_insights >> fim
    ver_historico >> fim
