import os

# Definindo as variáveis do projeto:
os.environ['envn'] = 'TEST'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

# Obtendo as variáveis do projeto:
envn = os.environ['envn']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

# appName para o Spark
appName = 'Expected Loss e Classificação com XGBoost'
caminho_atual = os.getcwd()
caminho_direto = os.path.dirname(caminho_atual)
caminho_kaggle = caminho_direto + '/Kaggle'
caminho_config = caminho_direto + '/config'
caminho_util = caminho_direto + '/util'
caminho_logs = caminho_util + '/arquivo_de_loggers.conf'
