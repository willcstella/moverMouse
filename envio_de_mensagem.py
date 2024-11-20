# COMO DIGITAR COM PYAUTOGUI
import pyautogui
import pyperclip # serve para colocar acentuações nas palavras

def escrever_frases(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# MOVER MOUSE ATÉ CAMPO DE DIGITAR
pyautogui.moveTo(1093, 702, duration=1)
# CLICAR NO CAMPO DIGITAR
pyautogui.click(button='left')
#DIGITAR MINHA MENSAGEM
# pyautogui.write('Olá. Bom dia.')
escrever_frases('Olá. Boa tarde.')

# CLICAR NO BOTÃO DE INVIAR
pyautogui.press('enter')
