import pickle
import os
import pandas as pd

ajusta_coluna = pd.set_option("display.max_columns", 100)
ajusta_largura = pd.set_option('display.width', 150)

path = os.path.dirname(__file__)
path_app = ajusta_path(path, 'app')
path_data = ajusta_path(path, 'data')
path_extract = ajusta_path(path_data, 'extract')
path_load = ajusta_path(path_data, 'load')
