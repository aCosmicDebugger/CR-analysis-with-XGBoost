import logging
import logging.config
import variaveis_do_projeto as varp
from pyspark.sql import SparkSession

# Carregando o arquivo de configuração de logging
logging.config.fileConfig(fname=varp.caminho_logs)
logger = logging.getLogger("criar_objeto")


def criar_objeto_spark(envn, appName):
    try:
        logger.info(f"obter_objeto_spark() foi criado. O '{envn}' envn foi usado.")
        if envn == 'TEST':
            master = 'local'
        else:
            master = 'yarn'

        spark = SparkSession \
            .builder \
            .master(master) \
            .appName(appName) \
            .getOrCreate()
    except NameError as ne:
        logger.error("ErrorName durante a criação do objeto Spark:" + str(ne),
                     exc_info=True)
        raise
    except ValueError as ve:
        logger.error("ValueError durante a criação do objeto Spark:" + str(ve),
                     exc_info=True)
        raise
    except Exception as e:
        logger.error("Ocorreu um erro durante a criação do objeto Spark:" + str(e),
                     exc_info=True)
        raise
    else:
        logging.info("Objeto Spark Criado.")

    return spark
