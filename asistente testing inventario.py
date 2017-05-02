import pyautogui, time

print('Buenas tardes compañero. Vamos a preparar los programas.')
time.sleep(1)
print('')
print("Ten abierto el archivo de word para apuntar")
print('los errores, y el excel con el inventario.')
time.sleep(2)
print('')
print('Ahora, con el documento excel en foco,')
print('pulsa windows+flecha izquierda,')
time.sleep(2)
print('')
print('y en el lado derecho pones este mismo programa')
print('abre el inventario y ajustas la ventana del programa')
print('para que puedas ver las dos ventanas a la vez.')
print('')
wait = input("Pulsa enter cuando estes listo.")

#print('de forma aproximada como se ve en la siguiente imagen')


ventanaInventario = 3, 70 #modificar este valor si la esquina se encuentra en otras coordenadas


time.sleep(1)
print('')
print('Recuerda que este programa se ha realizado en una')
print('pantalla de 1366x768, asi que tal vez tengas que modificar')
print('el valor de las coordenadas de la esquina superior izquierda')
print('de la primera ventana del inventario')
time.sleep(2)
print('')
print('por defecto el valor es: ', ventanaInventario)
print('')
time.sleep(0.5)
print('en 3 segundos')
time.sleep(1)
print('llevaremos el cursor a la esquina superior izquierda')
time.sleep(1)
print('de la ventana del inventario')
time.sleep(0.5)
print('3')
time.sleep(0.5)
print('2')
time.sleep(0.5)
print('1')
time.sleep(0.5)
pyautogui.moveTo(ventanaInventario)
time.sleep(0.5)
print('')

print('¿Coincide el cursor con la esquina superior izquierda de la ventana?')
coincide = input("contesta con una 's' para si y una 'n' para no:   ")
while coincide != 's':
    time.sleep(1)
    print('Introduce las coordenadas correctas de la esquina')
    X = input("introduce la primera coordenada:   ")
    Y = input("introduce la segunda coordenada:   ")
    time.sleep(1)
    ventanaInventario = int(X), int(Y)
    pyautogui.moveTo(ventanaInventario)
    print('¿Funciona ahora?')
    coincide = input("contesta con una 's' para si y una 'n' para no:   ")


#campo numerico incorrecto

time.sleep(0.5)
print('Perfecto, vamos a empezar')
time.sleep(0.5)
print('primero empezaremos poniendo el numero "6" en los campos numércos')
time.sleep(0.5)
print('recuerda haber tenido excel en foco justo antes de volver a esta pantalla ')
time.sleep(0.5)
wait = input("Pulsa enter cuando estes listo.")

pyautogui.PAUSE=0.4
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')

pyautogui.moveTo(ventanaInventario)
pyautogui.moveRel(107, 105)
pyautogui.doubleClick()

pyautogui.PAUSE=0

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('6')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.PAUSE=0.2
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')

#campos no 

print("")
print("¿Algun problema?")
print("Todos los campos tienen que estar en rojo")
print("Recuerda que si vas a apuntar un error en el office,")
print("tienes que volver a excel, antes de volver aqui")
print("Cuando pulses enter probaremos los")
print("caracteres no  numerico, p y ' ")
print("Se deber de poner todos en blanco")
wait = input("Pulsa enter cuando estes listo.")


pyautogui.PAUSE=0.4
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')


pyautogui.PAUSE=0

pyautogui.typewrite('Alumno 1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('3')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('2')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.PAUSE=0.2
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')


#campo numerico correcto

print("")
print("¿Algun problema?")
print("Todos los campos tienen que estar en rojo")
print("Recuerda que si vas a apuntar un error en el office,")
print("tienes que volver a excel, antes de volver aqui")
print("Cuando pulses enter probaremos los")
print("caracteres correctos para que todo se ponga verde")
wait = input("Pulsa enter cuando estes listo.")


pyautogui.PAUSE=0.4
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')


pyautogui.PAUSE=0

pyautogui.typewrite('Alumno 1')

pyautogui.('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('3')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('2')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite('1')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.PAUSE=0.2
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')



"""

pyautogui.PAUSE=0.2
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')

pyautogui.PAUSE=0
pyautogui.typewrite("Alumno1")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("1")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("3")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("2")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("1")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("1")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.typewrite("1")

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')

#campo vacío

print("")
print("¿Algun problema?")
print("Todos los campos tienen que estar en rosa")
print("Recuerda que si vas a apuntar un error en el office,")
print("tienes que volver a excel, antes de volver aqui")
print("Cuando pulses enter probaremos los caracteres no numericos 'p' y '")
print("caracteres no numericos 'p' y una coma simple")
wait = input("Pulsa enter cuando estes listo.")

pyautogui.PAUSE=0.2
pyautogui.keyDown('alt')#Para cambiar de programa
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')

pyautogui.PAUSE=0.5
pyautogui.hotkey('del')

pyautogui.click(876, 807)

"""

