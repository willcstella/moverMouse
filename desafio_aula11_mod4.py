# ALERTAR E PEDIR INFORMAÇÃO NO PYAUTOGUI
import pyautogui
import string
from time import sleep
# ALERTAR
# pyautogui.alert(text='Iniciando',title='Automação de Login',button='Ok')

# PEDIR INFORMAÇÃO

# email = pyautogui.prompt(text='Digite seu e-mail',title='Informações obrigatórias')

# print(f'Você digitou {email}')

# senha = pyautogui.password(text='Digite sua senha:',title='dados do login',mask='*')

# print(senha)

# CONFIRMAR SE ALGO DEVE OU NÃO DEVE ACONTER
# resposta = pyautogui.confirm(text='Continuar rodando a nossa aplicação ?',title='Confirmação',buttons=['sim','não','cancelar'])
# print(resposta) #testando resposta

# if resposta == 'sim':
#     print('continuando execução do app')
# elif resposta == 'não':
#     print('NÃO continuando execução do app')
# else:
#     print('cancelando execução do app')

####### DESAFIO #########
# Crie um programa que pede o usuário e senha e na sequência, copia e cola
# dentro de um bloco de notas
email= pyautogui.prompt(text='Digite seu e-mail:',title='Confirmação obrigatória')
senha = pyautogui.password(text='Digite sua senha:',title='Confirmação obrigatória',mask='*')

# MINIMIZAR O VS
pyautogui.click(1252,16,duration=2)
sleep(1)

# MOVER E CLICAR NO BLOCO DE NOTAS
pyautogui.click(997,109,duration=2)
sleep(1)

# ESCREVER O email
pyautogui.write(email)
# DAR ENTER
pyautogui.press('enter')
# # ESCREVER A SENHAR
pyautogui.write(senha)
# FECHARO APLICATIVO
pyautogui.click(1357,60,duration=2)
sleep(1)
# # SALVAR O ARQUIVO
pyautogui.click(606,394,duration=2)
sleep(1)