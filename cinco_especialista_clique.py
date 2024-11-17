# COMO USAR A FUNÇÃO CLICK
import pyautogui
# click personalizado
#pyautogui.click(x=850,y=464,clicks=100,interval=0.5,button='left', duration=5)

# Importa o mouseInfo do biblioteca mouse info no cmd
# python
#from mouseinfo import mouseInfo
#mouseInfo()

###### DESAFIO DE CRIAR UMA PASTA #######
# Deixar a tela do genrenciador de pastas maximizado

# 1 - MOVER O CURSOR AO CENTRO DA TELA
pyautogui.moveTo(1061,428,duration=1)

# 2 - CLICAR COM O BOTÃO DIREITO DO MOUSE
pyautogui.click(button='right', duration=1)

# 3 - MOVER ATÉ MENU NOVO
pyautogui.moveTo(1114, 382, duration=1)

# 4 - MOVER ATÉ A PASTA
pyautogui.moveTo(803,384, duration=2)

# 5 - CLICAR NA PASTA
pyautogui.click(button='left')

# 6 - MOVER ATÉ RENOMEAR
pyautogui.moveTo(447, 76, duration=2)

# 7 - CLICAR 
pyautogui.click(button='left')

# 8 - RENOMEAR
pyautogui.write('Pasta automatizada')

# 9 - APERTAR ENTER
pyautogui.press('enter')