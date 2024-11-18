
import pyautogui


###### TELA DE X = 1366 POR 768 #####


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

###### DESAFIO DE CRIAR COLOCAR ARQUIVOS EM UMA PASTA #######
# Deixar a tela do genrenciador de pastas maximizado
for arq in range(6):
    # 1 - MOVER O CURSOR AO CENTRO DA TELA
    pyautogui.moveTo(1061,428,duration=1)

    # 2 - CLICAR COM O BOTÃO DIREITO DO MOUSE
    pyautogui.click(button='right', duration=1)

    # 3 - MOVER ATÉ MENU NOVO
    pyautogui.moveTo(1114, 382, duration=1)

    # 4 - MOVER ATÉ DOCUMENTO DE TEXTO
    pyautogui.moveTo(859, 543, duration=1)

    # 5 - CLICAR COM O BOTÃO ESQUERDO DO MOUSE
    pyautogui.click(button='left')

    # 6 - RENOMEIA O ARQUIVO
    pyautogui.press('F2')

    # 7 - RENOMEAR
    pyautogui.write(f'Arquivo de texto{arq}')
for mover in range(6):
    # 8 - MOVER O CURSOR ATÉ O ARQUIVO
    pyautogui.moveTo(187, 236, duration=1)

    # 9 -  CLICAR E ARRASTAR O ARQUIVO
    pyautogui.dragTo(197, 211, duration=1)
