class AudioToText(object):
    def __init__(self, a):
        self.audio = a
        self.texto = None
        self.reload()

    def reload(self):
        self.texto = 'News FM 1234 hoje são dia 30 do 13 de 2019 às 15:13 a gente com virose minha conduta medicação oral e liberação para casa.'
