import pyautogui,time
pyautogui.PAUSE=0.5
pyautogui.FAILSAFE=True

#Para ver la posición:
#pyautogui.position()

#pyautogui.position()  Para obtener la posición del cursor.
#time.sleep(1)
#pyautogui.click(392, 13)
#time.sleep(1)
#pyautogui.doubleClick(549, 366)

#Para cambiar dos programas mas allá


#Pequeño programa para extraer el Numero de cliente y añadirlo a el documento de word.
#el programa capture2text debe estar abierto de fondo.
#Cuando el programa hay 20 segundos para ordenar los programas con alt+tab
#y remarcar el primer valor a copiar

#Posición de entrada del cursor para seleccionar numero de cliente


time.sleep(5)
times=1
while times<=4000:
    #en el documento de word
    pyautogui.hotkey('ctrl', 'c')#Copiar el texo
    pyautogui.PAUSE=0.5
    pyautogui.keyDown('alt')#Para cambiar de programa
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    
    #en el access
    pyautogui.hotkey('del')
    pyautogui.hotkey('ctrl', 'v') #para pegar el texto
    pyautogui.PAUSE=0
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.PAUSE=0.5
    
    
    pyautogui.moveTo(1059, 582)
    pyautogui.hotkey('win', 'q')
    pyautogui.moveTo(875, 556, duration=0.05)
    pyautogui.click(875, 556)

    pyautogui.keyDown('alt')#Para cambiar de programa
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    times=times+1

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')


"""
times=times+1
 pyautogui.hotkey('ctrl', 'v') #para pegar el texto
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.PAUSE=0.5
    pyautogui.moveTo((1062, 439), duration=0.05)
    pyautogui.hotkey('win', 'q')
    pyautogui.moveTo(738, 390, duration=0.05)
    pyautogui.click(738, 390)
    
    pyautogui.keyDown('alt')#Para cambiar de programa
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    times=times+1"""



    
    
    
    
