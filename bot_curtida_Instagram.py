# Bot de curtidas e comentários no Instagram com PyAutogui
# 1 – Navegar até o site https://www.instagram.com;
# 2 – Entrar com meu usuário;
# 3 – Entrar com a minha senha;
# 4 – Clicar em “log in”;
# 5 – Cicar em “Not now” para não salvar no navegador;
# 6 – Fechar janela de “salvar senha”;
# 7 – Entrar na página PESQUISAR;
# 8 – Clicar na PÁGINA PESQUISADA;
# 9 – Clicar na postagem mais recente;
# 10 – Verificar se já curti ou não aquela postagem;
# 11 – se já tiver curtido, fazer nada, e pausar bot por 24 horas;
# 12 -  se não tiver curtido, curtir a foto
# 13 – se não tiver curtido,comentar a foto;
# 14 -  Pausar por 24h;
# 15 – Após a 24h rodar tudo de novo;

import pyautogui
import webbrowser
from time import sleep
from PIL import Image

# 0 - Mimiza o vc
pyautogui.click(1253,18,duration=2)
sleep(2)
# 1 – Navegar até o site https://www.instagram.com;
webbrowser.open_new_tab('https://www.instagram.com')
sleep(5)
# 2 – Entrar com meu usuário;
pyautogui.click(786,289, duration=2)
sleep(1)
pyautogui.write('willcstella@gmail.com')
sleep(1)
# 3 – Entrar com a minha senha;
pyautogui.click(787,335, duration=2)
sleep(1)
pyautogui.write('@11Will64')
sleep(1)
# 4 – Clicar em “log in”;
pyautogui.click(886,381,duration=2)
sleep(5)
# 5 – Cicar em “Not now” para não salvar no navegador;
pyautogui.click(797,453,duration=2)
sleep(5)
# 6 – Fechar janela de “salvar senha”;
#   NÃO APARECEU NADA
# 7 – Clicar em PESQUISAR;
pyautogui.click(57,267,duration=2)
sleep(3)
pyautogui.write('devaprender')
sleep(2)
# 8 – Clicar na PÁGINA PESQUISADA;
pyautogui.click(175,253, duration=2)
sleep(2)
# 9 – Clicar na postagem mais recente;
pyautogui.click(496,705, duration=2)
sleep(2)
# 10 – Verificar se já curti ou não aquela postagem;
# 11 – se já tiver curtido, fazer nada, e pausar bot por 24 horas;
screenshot = pyautogui.screenshot()
sleep(1)
coracao = screenshot.getpixel((620,571))
coracao_curtido = (245,23,67)
coracao_nao_curtido = (255,255,255)
sleep(1)


if coracao_nao_curtido == coracao:
     pyautogui.click(619, 570,duration=2)
     sleep(1)
# #  # 13 – se não tiver curtido,comentar a foto;
     pyautogui.click(741,682,duration=2)
     sleep(1)
     pyautogui.write('Top! ;-)')
     sleep(1)
     pyautogui.click(1051,680,duration=2)
     sleep(1)
else:
     #sleep(43200)
     sleep(5)



pyautogui.click(225,617, duration=1)
sleep(1)
# #  fechar
pyautogui.click(46,677, duration=2)
sleep(2)
pyautogui.click(56,616, duration=2)
sleep(2)

