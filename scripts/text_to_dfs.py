import pandas as pd
from os.path import join as path_join
from os.path import isfile
from __config__ import path_dataframes


class TextToDfs(object):
    def __init__(self, t, k, c):
        self.text = t
        self.key = k
        self.customer = c
        self.insert_return = False
        self.reload()

    def reload(self):
        ''' TEXT MINING DO AUDIO '''
        extrai_crm = 1234
        extrai_ufcrm = None
        extrai_data = '2019-03-30 15:10:00'
        extrai_sintomas = None
        extrai_suspeita = 'virose'
        extrai_conduta = 'medicação oral, liberação para casa'
        extrai_medicacao = 'oral'

        ''' CRIACAO DOS DATAFRAMES'''
        df_audio = pd.DataFrame({'id': [self.key], 'phone': [self.customer], 'crm': [extrai_crm], 'ufcrm': [extrai_ufcrm], 'data': [extrai_data], 'text': [self.text]})
        df_sintomas = pd.DataFrame({'id': [self.key], 'crm': [extrai_sintomas]})
        df_suspeita = pd.DataFrame({'id': [self.key], 'crm': [extrai_suspeita]})
        df_conduta = pd.DataFrame({'id': [self.key], 'crm': [extrai_conduta]})
        df_medicacao = pd.DataFrame({'id': [self.key], 'crm': [extrai_medicacao]})

        ''' CONCATENAR '''
        def concat_df(df, name_file):
            path_full_df = path_join(path_dataframes, f'full_df_{name_file}.pkl')
            if isfile(path_full_df):
                full_df = pd.concat([pd.read_pickle(path_full_df), df]).reset_index(drop=True)
                full_df.to_pickle(path_full_df)
            else:
                df.to_pickle(path_full_df)
        concat_df(df_audio, 'url_do_audio')
        concat_df(df_sintomas, 'sintomas')
        concat_df(df_suspeita, 'suspeita')
        concat_df(df_conduta, 'conduta')
        concat_df(df_medicacao, 'medicacao')

        self.insert_return = True
