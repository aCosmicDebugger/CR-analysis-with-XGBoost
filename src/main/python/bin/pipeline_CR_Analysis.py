import os
import sys
import logging
import logging.config
import variaveis_do_projeto as varp
from criar_objeto import criar_objeto_spark
from validacao_dos_dados import obter_data_atual, print_Schema
from ingestao_dos_dados import carregar_dados

# from preprocess_dos_dados import limpeza_dos_dados

# Carregando o arquivo de configuração de logging
logging.config.fileConfig(fname=varp.caminho_logs)


def main():
    """
    main() é a função principal desse script. Ela faz a ingestão dos dados, faz a validação,
    cria um objeto Spark e valida esse objeto, faz a limpeza e transformação dos dados a
    serem usados tanto para o cálculo da Expected Loss quanto para o classificador XGBoost
    """
    logging.info("Iniciando o pipeline...")

    try:
        # Ingestão usando [ingestao_dos_dados.py]
        carregar_dados()

        # Criando objeto Spark [criar_objeto.py]
        objeto_spark = criar_objeto_spark(varp.envn, varp.appName)

        # Validar o objeto Spark criado [validação_dos_dados.py]
        obter_data_atual(objeto_spark)

        # Realizar operação de limpeza dos dados

        # Validar os dados processados

        # Transformar os dados

        # Validar os dados transformados


        logging.info("pipeline_CR_Analysis.py foi finalizado.")
    except Exception as exp:
        logging.error("Um erro ocorreu dentro da função principal. Cheque o stack-trace"
                      " e verifique o respectivo módulo " + str(exp), exc_info=True)

        sys.exit(1)


if __name__ == "__main__":
    logging.info("pipeline_CR_Analysis foi iniciado...")
    main()
