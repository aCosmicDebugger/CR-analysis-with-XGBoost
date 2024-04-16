import logging
import logging.config
import variaveis_do_projeto as varp
from tabulate import tabulate
from pyspark.sql import SparkSession

# Carregando o arquivo de configuração de logging
logging.config.fileConfig(fname=varp.caminho_logs)
logger = logging.getLogger(__name__)


def e_objeto_spark(objeto_spark):
    """
    Verifica se o objeto fornecido é uma instância de SparkSession.
    """
    return isinstance(objeto_spark, SparkSession)


def obter_data_atual(objeto_spark):
    """
    Usa a data atual para validar o objeto spark.
    """

    # Verifica se o objeto passado é um objeto Spark
    if not e_objeto_spark(objeto_spark):
        logger.error("O objeto passado não é uma instância de SparkSession.")
        raise ValueError("O objeto passado não é uma instância de SparkSession.")

    try:
        dataframe_saida = objeto_spark.sql("SELECT current_date")
        dados_spark = dataframe_saida.collect()

        for linha in dados_spark:
            data_atual = linha[0]
            # Formata a data como uma string no formato
            data_formatada = data_atual.strftime('%Y-%m-%d')
            print(f"Objeto Spark Criado, em {data_formatada}")
            logging.info("Validando o objeto Spark usando a data atual: %s", data_formatada)

        logging.info("Objeto Spark validado e pronto.")

    except Exception as e:
        logger.error("Erro ao validar o objeto Spark: %s", str(e))
        raise ValueError("Ocorreu um erro ao validar o objeto Spark usando a data atual.") from e


def print_Schema(dados, dataName):
    try:
        logger.info(f"Validação do Schema para o DataFrame {dataName}")
        sch = dados.schema.fields
        logger.info(f"O schema do DataFrame {dataName} é:")

        # Extrair informações do schema
        inform_scheema = [(field.name, field.dataType) for field in sch]

        # Criar tabela formatada
        tabela_scheema = tabulate(inform_scheema, headers=['Nome do Campo', 'Tipo de Dados'], tablefmt='pretty')

        # Imprimir tabela
        logger.info(f"\n{tabela_scheema}")

    except Exception as exp:
        logger.error("Erro na função print_Schema(). Cheque o stacktrace" + str(exp))
        raise
    else:
        logger.info("Validação do Schema foi completada.")
