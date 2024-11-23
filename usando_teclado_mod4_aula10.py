import pyautogui
import pyperclip
from time import sleep

def escrrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# navegar e clicar no campo LineEdit
pyautogui.click(1073,230,duration=2)
pyautogui.sleep(1)

escrrever_frase('WILLIAM CORRÊA DE OLIVEIRA STELLA; ***')
# dar um tab 
# PARA SABER QUAIS SÃO AS TECLAS DO TECLADO, SÓ USAR print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('tab')
pyautogui.sleep(1)
# pressionar enter
pyautogui.press('space')
