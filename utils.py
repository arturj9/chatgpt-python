import time

from gtts import gTTS
import os

def text_in_audio(text):
    
    try:

        tts = gTTS(text=text, lang='pt-br')
        tts.save('audio.mp3')

        os.system('mpg123 audio.mp3 2> /dev/null &')
        
        return 1
    
    except:
        
        return 0

def rm_audio():
    
    os.system('rm audio.mp3')

def efeito_digitação(texto):
    
    for letra in texto:
        
        print(letra, end='', flush=True)
        
        time.sleep(0.09)