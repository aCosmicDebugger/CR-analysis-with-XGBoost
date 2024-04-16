import os
import variaveis_do_projeto as varp

def criar_arquivo_de_loggers_config():
    caminho_config_log = os.path.join(varp.caminho_config, 'config_logs.txt')
    print(caminho_config_log)

    with open(caminho_config_log, 'r') as file:
        conteudo_config = file.read()

    # Adicionar os argumentos para a opção args do manipulador de arquivo fileHandler
    nova_opcao_args = "args = ('" + os.path.join(varp.caminho_direto, 'logs', 'pipeline.logs') + "', 'a')"
    conteudo_config = conteudo_config.replace('args =', nova_opcao_args)

    # Criar o diretório de logs, se não existir
    logs_dir = os.path.join(varp.caminho_direto, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Criar a pasta util, se não existir
    util_dir = varp.caminho_util
    if not os.path.exists(util_dir):
        os.makedirs(util_dir)

    # Escrever o novo conteúdo no arquivo de configuração
    with open(os.path.join(util_dir, 'arquivo_de_loggers.conf'), 'w') as file:
        file.write(conteudo_config)

def main():
    util_dir = varp.caminho_util
    config_loggers = os.path.join(util_dir, 'arquivo_de_loggers.conf')

    if not os.path.exists(config_loggers):
        criar_arquivo_de_loggers_config()
        print("Arquivo de configuração de loggers criado com sucesso.")
    else:
        print("Arquivo de configuração de loggers já existe.")

if __name__ == "__main__":
    main()
