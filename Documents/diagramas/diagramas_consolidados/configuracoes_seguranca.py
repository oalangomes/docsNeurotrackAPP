from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.programming.flowchart import Action, Decision, InputOutput, Database
from diagrams.aws.security import Shield, IAM
from diagrams.aws.storage import S3
from diagrams.programming.language import Python

# Criar diagrama consolidado para Configurações de Segurança
with Diagram("Configurações de Segurança - NeurotrackApp", show=False, direction="TB", filename="configuracoes_seguranca_consolidado"):
    
    # Nós iniciais e finais
    inicio = Action("Início")
    fim = Action("Fim")
    
    # Usuário
    usuario = User("Usuário")
    
    # Fluxo principal
    acessar_app = Action("Acessar app\nNeurotrack")
    acessar_secao = Action("Acessar seção\nConfigurações de Segurança")
    
    # Opções de segurança
    with Cluster("Opções de Segurança"):
        gerenciar_autenticacao = Action("Gerenciar métodos\nde autenticação")
        configurar_privacidade = Action("Configurar opções\nde privacidade")
        gerenciar_dados = Action("Gerenciar dados\npessoais")
    
    # Gerenciamento de autenticação
    with Cluster("Gerenciamento de Autenticação"):
        alterar_senha = Action("Alterar senha")
        configurar_biometria = Action("Configurar\nbiometria")
        ativar_2fa = Action("Ativar autenticação\nde dois fatores")
        gerenciar_sessoes = Action("Gerenciar sessões\nativas")
    
    # Configurações de privacidade
    with Cluster("Configurações de Privacidade"):
        definir_visibilidade = InputOutput("Definir visibilidade\nde dados")
        compartilhamento_dados = InputOutput("Configurar compartilhamento\ncom profissionais")
        permissoes_app = InputOutput("Gerenciar permissões\ndo aplicativo")
        notificacoes_seguranca = Action("Configurar notificações\nde segurança")
    
    # Gerenciamento de dados pessoais
    with Cluster("Gerenciamento de Dados Pessoais"):
        visualizar_dados = InputOutput("Visualizar dados\narmazenados")
        exportar_dados = Action("Exportar todos\nos dados")
        solicitar_exclusao = Action("Solicitar exclusão\nde dados")
        backup_dados = Action("Configurar backup\nautomático")
    
    # Componentes de segurança
    sistema_autenticacao = IAM("Sistema de\nAutenticação")
    sistema_criptografia = Shield("Sistema de\nCriptografia")
    sistema_backup = S3("Sistema de\nBackup")
    
    # Banco de dados
    db_usuarios = Database("Banco de Dados\nde Usuários")
    db_configuracoes = Database("Banco de Dados\nde Configurações")
    
    # Conexões do fluxo principal
    inicio >> usuario >> acessar_app >> acessar_secao
    
    # Opções principais
    acessar_secao >> gerenciar_autenticacao
    acessar_secao >> configurar_privacidade
    acessar_secao >> gerenciar_dados
    
    # Gerenciamento de autenticação
    gerenciar_autenticacao >> alterar_senha
    gerenciar_autenticacao >> configurar_biometria
    gerenciar_autenticacao >> ativar_2fa
    gerenciar_autenticacao >> gerenciar_sessoes
    
    # Configurações de privacidade
    configurar_privacidade >> definir_visibilidade
    configurar_privacidade >> compartilhamento_dados
    configurar_privacidade >> permissoes_app
    configurar_privacidade >> notificacoes_seguranca
    
    # Gerenciamento de dados pessoais
    gerenciar_dados >> visualizar_dados
    gerenciar_dados >> exportar_dados
    gerenciar_dados >> solicitar_exclusao
    gerenciar_dados >> backup_dados
    
    # Conexões com componentes de segurança
    alterar_senha >> sistema_autenticacao
    configurar_biometria >> sistema_autenticacao
    ativar_2fa >> sistema_autenticacao
    gerenciar_sessoes >> sistema_autenticacao
    
    definir_visibilidade >> sistema_criptografia
    compartilhamento_dados >> sistema_criptografia
    
    exportar_dados >> sistema_backup
    backup_dados >> sistema_backup
    
    # Interações com banco de dados
    sistema_autenticacao >> db_usuarios
    sistema_criptografia >> db_configuracoes
    visualizar_dados >> db_usuarios
    solicitar_exclusao >> db_usuarios
    
    # Finalização
    alterar_senha >> fim
    ativar_2fa >> fim
    notificacoes_seguranca >> fim
    exportar_dados >> fim
    solicitar_exclusao >> fim
    backup_dados >> fim
