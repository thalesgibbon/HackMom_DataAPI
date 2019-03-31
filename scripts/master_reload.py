''' RELOAD PRINCIPAL '''
from scripts.audio_to_text import AudioToText
from scripts.text_to_dfs import TextToDfs
from os.path import join as path_join
from __config__ import path_audios
import urllib


class MasterReload(object):
    def __init__(self, k, c, a):
        self.key = k
        self.customer = c
        self.url_do_audio = a
        self.path_do_audio = path_join(path_audios, f'{self.key}.oga')
        self.insert_return = False
        self.reload()

    def reload(self):
        urllib.request.urlretrieve(self.url_do_audio, self.path_do_audio)

        text = AudioToText(a=self.path_do_audio).texto

        self.insert_return = TextToDfs(t=text, k=self.key, c=self.customer)

        self.insert_return = True


if __name__ == '__main__':
    customer = 5551984442801
    audio = None
    key = 123456
    r = MasterReload(k=key, c=customer, a=audio)
    print(r.insert_return)
