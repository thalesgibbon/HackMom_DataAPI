import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from __config__ import path


class AudioToText(object):
    def __init__(self, a):
        self.audio = a
        self.texto = None
        self.reload()

    def reload(self):

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(path, "google_key.json")
        client = speech.SpeechClient()

        with io.open(self.audio, 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)

        _, extension = os.path.splitext(self.audio)
        if extension == '.flac':
            encoding = enums.RecognitionConfig.AudioEncoding.FLAC
        elif extension in ['.opus', '.oga']:
            encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
        else:
            encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
        config = types.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=16000,
            language_code='pt-BR')

        try:
            response = client.recognize(config, audio)
            transcript = response.results[0].alternatives[0].transcript
        except Exception as e:
            transcript = 'Error: %s' % e

        self.texto = transcript


if __name__ == '__main__':
    audio = r'C:\projetos\HackMom_DataAPI\files\audios\123456789_20190331_040857333013.oga'
    r = AudioToText(a=audio).texto
    print(r)
