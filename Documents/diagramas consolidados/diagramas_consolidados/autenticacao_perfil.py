from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.onprem.network import Internet
from diagrams.programming.language import Python

# Criar diagrama consolidado para Autenticação e Perfil
with Diagram("Autenticação e Perfil do Usuário - NeurotrackApp", show=False, direction="TB", filename="autenticacao_perfil_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Fluxo principal de autenticação
    acessar_app = Action("Acessar app\nNeurotrack")
    possui_conta = Decision("Já possui\nconta?")
    
    # Opções de login
    with Cluster("Opções de Login"):
        login_email = Action("Login com\ne-mail e senha")
        login_google = Action("Login com\nGoogle")
        login_biometria = Action("Login com\nbiometria")
    
    # Cadastro de novo usuário
    with Cluster("Cadastro de Novo Usuário"):
        cadastro_dados = InputOutput("Preencher dados\nde cadastro")
        cadastro_perfil = InputOutput("Configurar perfil\nneurodivergente")
        cadastro_preferencias = InputOutput("Definir preferências\nde interação")
    
    # Autenticação e validação
    autenticar = Action("Autenticar\ncredenciais")
    validar_token = Action("Validar token\nJWT")
    
    # Gerenciamento de perfil
    with Cluster("Gerenciamento de Perfil"):
        visualizar_perfil = InputOutput("Visualizar perfil")
        editar_perfil = Action("Editar dados\ndo perfil")
        atualizar_senha = Action("Atualizar\nsenha")
        editar_neuro_perfil = Action("Editar perfil\nneurodivergente")
        gerenciar_preferencias = Action("Gerenciar\npreferências")
    
    # Banco de dados
    db_usuarios = Database("Banco de Dados\nde Usuários")
    
    # Conexões do fluxo principal
    inicio >> acessar_app >> possui_conta
    possui_conta >> login_email >> autenticar
    possui_conta >> login_google >> autenticar
    possui_conta >> login_biometria >> autenticar
    
    # Fluxo de cadastro (caminho "Não")
    possui_conta >> Edge(label="Não") >> cadastro_dados >> cadastro_perfil >> cadastro_preferencias >> autenticar
    
    # Autenticação e validação
    autenticar >> validar_token
    
    # Interações com banco de dados
    autenticar >> db_usuarios
    cadastro_dados >> db_usuarios
    editar_perfil >> db_usuarios
    atualizar_senha >> db_usuarios
    editar_neuro_perfil >> db_usuarios
    
    # Fluxo de gerenciamento de perfil
    validar_token >> visualizar_perfil
    visualizar_perfil >> editar_perfil
    visualizar_perfil >> atualizar_senha
    visualizar_perfil >> editar_neuro_perfil
    visualizar_perfil >> gerenciar_preferencias
    
    # Finalização
    validar_token >> fim
    editar_perfil >> fim
    atualizar_senha >> fim
    editar_neuro_perfil >> fim
    gerenciar_preferencias >> fim
