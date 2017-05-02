import pyautogui, pyperclip, time
time.sleep(5)

pyautogui.click(176, 268)

pyautogui.hotkey('ctrl', 'c')
titularExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
direccionExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
telefonoFijoExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
telefonoMovilExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
codigoPostalExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
provinciaExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
numeroExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
pisoExcel=pyperclip.paste()
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'c')
puertaExcel=pyperclip.paste()
pyautogui.hotkey('tab')

print("titular:", titularExcel, " dirección:", direccionExcel, " numero:", numeroExcel, " piso:", pisoExcel, " puerta", puertaExcel, " codigo postal:", codigoPostalExcel, " provincia:", provinciaExcel, " telefono fijo:", telefonoFijoExcel, " telefono movil", telefonoMovilExcel)


