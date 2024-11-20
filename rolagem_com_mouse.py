#  COMO SIMULAR ROLAGEM COM O MOUSE #
# QUE VAI ATÉ A SESSÃO HISTÓRIA     #
# https://pt.wikipedia.org/wiki/Brasil?_gl=1*f7vc2i*_ga*MTE0NzI5OTk2Ni4xNzMxMDIyNjUz*_ga_37GXT4VGQK*MTczMjEwODQyNS4yNy4xLjE3MzIxMDk0MjYuMC4wLjA.


import pyautogui

from time import sleep

# MOVE ATÁ A PARTE CENTRAL DA PÁGINA.
pyautogui.moveTo(x=1061,y=428,duration=2)

for i in range(5):
    pyautogui.scroll(-600)
    sleep(1)

