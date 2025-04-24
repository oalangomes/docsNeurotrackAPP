from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.compute import Server
from diagrams.gcp.api import APIGateway
from diagrams.programming.language import Python

# Criar diagrama consolidado para Integração com Agenda
with Diagram("Integração com Agenda - NeurotrackApp", show=False, direction="TB", filename="integracao_agenda_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nAgenda")
    
    # Opções de agenda
    with Cluster("Opções de Agenda"):
        criar_evento = Action("Criar novo\nevento")
        visualizar_eventos = Action("Visualizar\ncalendário")
        filtrar_eventos = Action("Filtrar eventos\npor categoria/data")
    
    # Criação de evento
    with Cluster("Criação de Evento"):
        titulo_evento = InputOutput("Definir título\ndo evento")
        data_evento = InputOutput("Selecionar data")
        hora_evento = InputOutput("Definir horário")
        local_evento = InputOutput("Adicionar local\n(opcional)")
        categoria_evento = InputOutput("Selecionar categoria\n(consulta, compromisso)")
        adicionar_lembrete = Action("Configurar\nlembretes")
        adicionar_recorrencia = Action("Definir recorrência\n(opcional)")
    
    # Gerenciamento de eventos
    with Cluster("Gerenciamento de Eventos"):
        ver_detalhes = InputOutput("Ver detalhes\ndo evento")
        editar_evento = Action("Editar evento\nexistente")
        excluir_evento = Action("Excluir evento")
        marcar_concluido = Action("Marcar como\nconcluído")
    
    # Integração com Google Calendar
    with Cluster("Integração com Google Calendar"):
        autenticar_google = Action("Autenticar com\nGoogle")
        autorizar_acesso = Decision("Autorizar acesso\nao calendário?")
        sincronizar_eventos = Action("Sincronizar\neventos")
        importar_eventos = Action("Importar eventos\ndo Google")
        exportar_eventos = Action("Exportar eventos\npara Google")
    
    # Serviços externos
    google_calendar = Server("Google Calendar\nAPI")
    
    # Banco de dados
    db_eventos = Database("Banco de Dados\nde Eventos")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> criar_evento
    acessar_secao >> visualizar_eventos
    acessar_secao >> filtrar_eventos
    
    # Fluxo de criação
    criar_evento >> titulo_evento >> data_evento >> hora_evento >> local_evento >> categoria_evento
    categoria_evento >> adicionar_lembrete
    adicionar_lembrete >> adicionar_recorrencia
    adicionar_recorrencia >> db_eventos
    
    # Fluxo de visualização e gerenciamento
    visualizar_eventos >> ver_detalhes
    ver_detalhes >> editar_evento
    ver_detalhes >> excluir_evento
    ver_detalhes >> marcar_concluido
    
    # Interações com banco de dados
    editar_evento >> db_eventos
    excluir_evento >> db_eventos
    marcar_concluido >> db_eventos
    
    # Integração com Google Calendar
    acessar_secao >> autenticar_google >> autorizar_acesso
    autorizar_acesso >> Edge(label="Sim") >> sincronizar_eventos
    sincronizar_eventos >> importar_eventos
    sincronizar_eventos >> exportar_eventos
    
    # Conexões com Google Calendar
    importar_eventos >> db_eventos
    db_eventos >> exportar_eventos
    importar_eventos << google_calendar
    exportar_eventos >> google_calendar
    
    # Finalização
    adicionar_recorrencia >> fim
    marcar_concluido >> fim
    excluir_evento >> fim
    exportar_eventos >> fim
