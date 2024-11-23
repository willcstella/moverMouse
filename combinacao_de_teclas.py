import pyautogui
import pyperclip

from time import sleep

def escrrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')


# PARA AVISR QUE A AUTOMAÇÃO ESTÁ INICIANDO
pyautogui.alert(text='iniciando a automação',title='Automação', button='Ok')

# pedindo confirmação
 
resposta = pyautogui.confirm(texto='Continuar rodando nossa aplicação?', Buttons=['sim','não','cancelar'])
print(resposta)
# PEDINDO INFORMAÇÕES PARA O USUÁRIO
texto = pyautogui.prompt(text='digito texto a ser inserido.')
print(texto)
# pyautogui.click(1085,110, duration=2)
# sleep(1)
'''
pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('a')

É A MESMA COISA QUE

pyautogui.hotkey('ctrl','a')

'''
# pyautogui.hotkey('ctrl','a')
# pyautogui.hotkey('ctrl','c')

# pyautogui.click(1106,275, duration=2)
# sleep(1)

# pyautogui.hotkey('ctrl','v')
# sleep(1)

# # dar um tab 
# # PARA SABER QUAIS SÃO AS TECLAS DO TECLADO, SÓ USAR print(pyautogui.KEYBOARD_KEYS)
# pyautogui.press('tab')
# pyautogui.sleep(1)
# # pressionar enter
# pyautogui.press('space')
