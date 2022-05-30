import win32gui
import win32ui
import time
from ctypes import windll
from PIL import Image
from PySimpleGUI import PySimpleGUI as sg
from threading import Thread

state = False
winOpen = True

timeSet = 60
path = r'C:\temp'
alvo = 'Calculadora'
arqNome = 'temp.jpeg'

def screenshot():
    hwnd = win32gui.FindWindow(None, alvo)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        im.save(f"{path}/{arqNome}")

def window():
    sg.theme('LightBlue')
    global winOpen
    
    layout = [[sg.Button('Tirar foto agora'), sg.Text(size=(15,1), key='-FOTO-')],
            [sg.Text('Tempo entre updates (Segundos):'), 
            sg.Text(size=(15,1), key='-OUTPUT-')], 
            [sg.Input(key='-IN-',default_text='60'), sg.Button('Mudar tempo')],
            [sg.Text('Nome do arquivo:'), sg.Text(size=(15,1), key='-OUT_ARQ-')],
            [sg.Input(key='-IN_ARQ-', default_text='temp.jpeg'), sg.Button('Definir')],
            [sg.Text('Programa alvo (Nome exato):'), sg.Text(size=(15,1), key='-OUT_ALVO-')],
            [sg.Input(key='-IN_ALVO-', default_text='Calculadora'), sg.Button('Mudar alvo')],
            [sg.Button('Iniciar/Pausar Programa'), sg.Text(size=(15,1), key='-STATE-')],
            [sg.Button('Sair')]]
    
    window = sg.Window('AutoScreenshot', layout) 
    
    
    try:
        while True: 
            event, values = window.read() 
            global state, timeSet, alvo, arqNome

            if event == 'Tirar foto agora':
                window['-FOTO-'].update('Foto feita')
                screenshot()

            if event in  (None, 'Sair'): 
                state = False
                winOpen = False
                break
            
            if event == 'Mudar tempo': 
                try:
                    int(values['-IN-'])
                    e_num = True
                except ValueError:
                    e_num = False
                
                if e_num:
                    window['-OUTPUT-'].update(values['-IN-'])
                    timeSet = int(values['-IN-'])
            
            if event == 'Definir':
                window['-OUT_ARQ-'].update(values['-IN_ARQ-'])
                arqNome = values['-IN_ARQ-']
            
            if event == 'Mudar alvo': 
                window['-OUT_ALVO-'].update(values['-IN_ALVO-'])
                alvo = values['-IN_ALVO-']

            if event == 'Iniciar/Pausar Programa':
                if state == False:
                    state = True
                    window['-STATE-'].update('Ligado')
                else:
                    state = False
                    window['-STATE-'].update('Desligado')

        
        window.close()
    except:
        winOpen = False
        sg.popup_error(f'ERRO. Tente novamente.')


Thread(target = window).start() 
while True:
    if state:
        while state:
            time.sleep(timeSet)
            if state:
                screenshot()

    if not winOpen:
        break

    time.sleep(3)
