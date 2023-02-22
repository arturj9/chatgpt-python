from gtts import gTTS #Tratamento de ádio
import os
import time


def text_in_audio(text):
    '''
    Converte texto em áudio, salva em audio.mp3 e reproduz esse.
    '''
    try:
        # Converte o conteúdo de text em áudio.
        tts = gTTS(text=text, lang='pt-br')
        
        # Salva o coteúdo do áudio em audio.mp3.
        tts.save('audio.mp3')

        # Reproduz audio.mp3 em segundo plano.
        os.system('mpg123 audio.mp3 2> /dev/null &')

        return 1

    except:
        
        return 0

def rm_audio():
    '''
    Remove o arquivo audio.mp3.
    '''
    try:
        os.system('rm audio.mp3')
        
        return 1
    
    except:
        
        return 0

def typing_effect(texto):
    '''
    Produz o efeito de digitação.
    '''
    try:
        for letra in texto:

            print(letra, end='', flush=True)

            time.sleep(0.09)
            
        return 1
    
    except:
        
        return 0

        