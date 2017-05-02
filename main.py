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
    time.sleep(0.6) #He puesto esta linea para que espere 6 segundos después
                    #de cambiar de programa, puede eliminarse o ajustarse en diferentes
                    #configuraciones"""

#En word, para cambiar cada celda de la tabla en la que se encuentran los datos

def cambiarCeldaWord(numeroDeCeldas):
    pyautogui.PAUSE=0.3
    for i in range(numeroDeCeldas):
        pyautogui.keyDown('tab')

#para copiar el texto

def copiar():
    pyautogui.hotkey('ctrl', 'c')

#para pegar el texto

def pegar():
    pyautogui.hotkey('ctrl', 'v')

#cambiarPrograma(2)
#copiar()
#cambiarCeldaWord(6)
#pegar()
