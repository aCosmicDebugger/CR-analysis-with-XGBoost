import os
import logging.config
import variaveis_do_projeto as varp
from kaggle.api.kaggle_api_extended import KaggleApi

# Carregando o arquivo de configuração do log
logging.config.fileConfig(fname=varp.caminho_logs)
logger = logging.getLogger("ingestao_dos_dados")


def carregar_dados():
    """
    Faz o download dos conjunto de dados usando a API do Kaggle
    """

    # Autenticação
    api = KaggleApi()
    api.authenticate()

    # Identificador do conjunto de dados no Kaggle
    id_dos_dados = 'adarshsng/lending-club-loan-data-csv'

    # Verifica se o diretório existe e cria, se necessário
    if not os.path.exists(varp.caminho_kaggle):
        os.makedirs(varp.caminho_kaggle)
        logger.info(f"Criado o diretório: {varp.caminho_kaggle}")
        print(f"Criado o diretório: {varp.caminho_kaggle}")

    # Verifica se os arquivos já existem no caminho especificado
    arquivos = os.listdir(varp.caminho_kaggle)
    if arquivos:
        logger.info(f"Os arquivos já existem em: {varp.caminho_kaggle}")
        print(f"Os arquivos já existem em: {varp.caminho_kaggle}")
    else:
        logger.info("Fazendo o download dos dados...")
        print("Fazendo o download dos dados...")
        try:
            api.dataset_download_files(id_dos_dados, path=varp.caminho_kaggle, unzip=True)
        except Exception as e:
            logger.error(f"Um erro ocorreu ao tentar fazer o download do arquivo: {str(e)}", exc_info=True)
        else:
            logger.info(f"Arquivos baixados em: {varp.caminho_kaggle}")
            print(f"Arquivos baixados em: {varp.caminho_kaggle}")


if __name__ == "__main__":
    carregar_dados()
