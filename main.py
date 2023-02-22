from openai_api import openai_response, os
from utils import efeito_digitação, text_in_audio, rm_audio

import random

greetings = ['Olá!', 'Oi.', 'E aí...']

os.system('cls' if os.name == 'nt' else 'clear')

print(f'\n{greetings[random.randint(0, len(greetings))-1]}')

inital_questions = ['Como posso ajudar?', 'Qual sua dúvida?', 'Informe seu questionamento:',
                    'Como posso seu útil?', 'Pergunte algo:']

while(1):

    print(f'\n{inital_questions[random.randint(0, len(inital_questions))-1]}')
    print('\n** Digite s para sair **\n')

    question = input()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if question.lower() == 's':
        print('\nSaindo...\n')
        break
    
    print('Aguarde...')

    response = openai_response(question)
    
    if not text_in_audio(response):
        os.system('cls' if os.name == 'nt' else 'clear')        
        print('Error...')
        break
    
    efeito_digitação(f'{response}\n')
    
    rm_audio()