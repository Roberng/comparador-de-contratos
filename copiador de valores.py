import pyautogui, time, pyperclip

#para coppiar el titular

pyautogui.click(287, 273)

pyautogui.click(287, 273)

pyautogui.click(287, 273)

pyautogui.hotkey('ctrl', 'c')

titularExcel = pyperclip.paste()
print(titularExcel)

time.sleep(1)

#para coppiar la dirección
pyautogui.hotkey('tab') 
pyautogui.hotkey('ctrl', 'c')

direccionExcel = pyperclip.paste()
print(direccionExcel)

time.sleep(1)

#para coppiar el numero 
pyautogui.click(181, 431)
pyautogui.click(181, 431)
pyautogui.click(181, 431)
pyautogui.hotkey('ctrl', 'c')

numeroExcel = pyperclip.paste()
print(numeroExcel)

time.sleep(1)

#para coppiar el numero 
pyautogui.click(181, 431)
pyautogui.click(181, 431)
pyautogui.click(181, 431)
pyautogui.hotkey('ctrl', 'c')

numeroExcel = pyperclip.paste()
print(numeroExcel)

time.sleep(1)
