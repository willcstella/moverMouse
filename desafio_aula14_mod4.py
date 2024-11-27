# DESAFIO 🥇
# 1) Navegue até o site https://cursoautomacao.netlify.app/
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
# 3) Clique em alerta, para gerar a alerta
# 4) Feche a alerta
# 5) Suba a página totalmente para cima
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"

import pyautogui
import webbrowser
from time import sleep

webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
sleep(2)
# MINIMIZAR O VC
#pyautogui.click(1252,18,duration=1)

# Mover para dentro da pagina
pyautogui.moveTo(1191, 161, duration=2)
sleep(1)
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.scroll(-850)
pyautogui.click(1068,407, duration=1)
pyautogui.write('Bill Star')
# 3) Clique em alerta, para gerar a alerta
pyautogui.click(1044,442, duration=1)
# 4) Feche a alerta
pyautogui.click(858,187, duration=1)
# 5) Suba a página totalmente para cima
pyautogui.scroll(850)
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos
# para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
pyautogui.scroll(-1850)
pyautogui.click(223,549, duration=1)
sleep(1)
pyautogui.click(398,551, duration=1)
sleep(1)
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU')
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.press('space')

#pyautogui.click(694,438, duration=2)
