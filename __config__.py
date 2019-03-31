import os
import pandas as pd

ajusta_coluna = pd.set_option("display.max_columns", 100)
ajusta_largura = pd.set_option('display.width', 150)

path = os.path.dirname(__file__)
path_files = path + r'\files'
path_audios = path_files + r'\audios'
path_dataframes = path_files + r'\dataframes'

