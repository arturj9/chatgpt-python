from utils import typing_effect, text_in_audio, rm_audio
from openai_api import openai_response, os
import random

# Saudações.
greetings = ['Olá!', 'Oi.', 'E aí...']

# Questionamentos iniciais.
inital_questions = ['Como posso ajudar?', 'Qual sua dúvida?', 'Informe seu questionamento:',
                    'Como posso seu útil?', 'Pergunte algo:']


# Limpar terminal.
os.system('cls' if os.name == 'nt' else 'clear')

# Imprime uma saudação de forma aleatória.
print(f'\n{greetings[random.randint(0, len(greetings))-1]}')

while(1):
    
    # Imprime um questionamento inicial de forma aleatória.
    print(f'\n{inital_questions[random.randint(0, len(inital_questions))-1]}')
    
    print('\n** Digite s para sair **\n')

    question = input()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Sair do programa.
    if question.lower() == 's':
        print('\nSaindo...\n')
        break
    
    print('Aguarde...')

    # Tenta obter uma resposta da api da OpenAI dado um questionamento.
    response = openai_response(question)
    
    # Converter texto da resposta em aúdio e reproduzi-lo.
    if not text_in_audio(response):
        os.system('cls' if os.name == 'nt' else 'clear')        
        print('Error...')
        break
    
    # Exibe o texto da resposta no efeito de digitação.
    typing_effect(f'{response}\n')
    
    # Apaga o audio criado.
    rm_audio()