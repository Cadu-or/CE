from mesa.batchrunner import BatchRunner
from .model import *

'''
Geracao de arquivo csv com os dados armazenados.
'''
def getData():
    model = AreaNetwork(9)      # Criacao de modelo
    for _ in range(15):         # Definicao de 15 steps
        model.step()

    model_df = model.datacollector.get_model_vars_dataframe() # Coleta de dados para a construcao do dataframe
    model_df.to_csv(path_or_buf="DataFrame.csv")              # Criacao do arquivo CSV