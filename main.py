#!/usr/bin/env python3

import pyautogui, time

#Con esta función cambiamos de programa,poniendo entre parentesis
#el número de la posición que se encuentra al fondo de programas abiertos.

def cambiarPrograma(numeroDeProgramas):
    pyautogui.PAUSE=0.1
    pyautogui.keyDown('alt')
    vecesParaCambiar = 0
    while vecesParaCambiar < numeroDeProgramas:
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        vecesParaCambiar = vecesParaCambiar+1
    pyautogui.keyUp('alt')



