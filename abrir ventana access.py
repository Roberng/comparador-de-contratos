import pywinauto

pwa_app = pywinauto.application.Application()
w_handle = pywinauto.findwindows.find_windows(title=u'Settings', class_name='ApplicationFrameWindow')[0]
window = pwa_app.window_(handle=w_handle)
window.SetFocus()

