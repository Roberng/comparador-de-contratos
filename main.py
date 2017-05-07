#!/usr/bin/env python3

import pyautogui, time, pyperclip, logging, os

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.disabled = False

#Esta es una función de seguridad, para que no haya ninguna tecla marcada

#def seguridad():
#    pyautogui.keyUp('tab')
#    pyautogui.keyUp('alt')
#    pyautogui.keyUp('ctrl')
#    print('teclas desactivadas')


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
    pyautogui.PAUSE=0
    for i in range(numeroDeCeldas):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')

#para copiar el texto

def copiar():
    pyautogui.PAUSE=0.01
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

#para pegar el texto

def pegar():
    pyautogui.hotkey('ctrl', 'v')

# esta función asigna una variable y le da como valor lo que
# haya en el portapapeles y lo pega (append) en un archivo de texto

def introducirContratos():
    idCnotrato = pyperclip.paste()
    with open("id_contratos.txt", "a") as myfile:
        myfile.write(idCnotrato+'\n')
        logger.warning('valor copiado: ' + idCnotrato)
        myfile.close()

def borrar():
    os.remove("id_contratos.txt")
    safe()
    
#El programa comienza aqui


open("id_contratos.txt", "w")

    
logger.info('Cambia al ultimo programa de fondo')
cambiarPrograma(2)

logger.info('pone el contador a cero')
contador = 0
time.sleep(0.1)
while contador < 300 :
    logger.info('empezamos el bucle')
    
    time.sleep(0.08)

    logger.info('copiamos el valor resaltado')
    copiar()

    logger.info('pasamos el valor copiado del portapapeles a un id_id_contratos.txt')
    introducirContratos()

    logger.info('cambiamos cuatro celdas')
    cambiarCeldaWord(4)
     
    logger.info('sumamos 1 a contador')
    contador = contador + 1
    quedando = 4000 - contador
    logger.info('quedan: ' + str(quedando) + ' valores')

    
logger.info('terminamos el bucle')
