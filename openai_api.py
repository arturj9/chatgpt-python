from dotenv import load_dotenv
import os

import openai

load_dotenv()

# Chave da api (.env).
openai.api_key = os.getenv('OPENAI_API_KEY')

def openai_response(text):
    '''
    Obtem uma resposta da api da OpenAi, a partir de um texto informado.
    '''
    try:

        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=text,
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )

        return response['choices'][0]['text']
    
    except:
        
        return 'Erro ao tentar obter resposta.'

