import os
import time
import pyautogui

def pausa (seg):
    for i in range(seg,0,-1):
        print(f"{i}  ", end="\r")
        time.sleep(1)
    
#funcion on/off wifi  
#ver name: netsh interface show interface
def wifi(modo): 
    if modo=='on':
        os.system('netsh wlan connect md1')
        pausa(30)
    elif modo=='off':
        time.sleep(30)
        os.system('netsh wlan disconnect')

def wifienova():
    pyautogui.click(1820,1055)
    time.sleep(3)
    pyautogui.click(1530,990)
    time.sleep(3)
    pyautogui.click(1530,990)
    time.sleep(30)
    pyautogui.click(900,530)

def cerrarvent():
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    time.sleep(3)

while True:
    wifi('on')
    #wifienova()

    os.system("cls")
    
    #os.system("start chrome https://mdchi.github.io/visor/noticias.html")  #investing noticias
    #os.system("start chrome https://coinmarketcap.com/watchlist/665296ac3a9fc91e643242c9/")   #activo
    #os.system("start chrome https://coinmarketcap.com/watchlist/6623cb7071fbad387354cd39/")  #analisis1
    #os.system("start chrome https://coinmarketcap.com/watchlist/662100fee5333e1cf1bd47ce/")  #analisis2
    #os.system("start chrome https://coinmarketcap.com/watchlist/67191b3ad1a6dc6ec8433700/")   #analisis3
    #os.system("start chrome https://dolarhoy.com/historico-dolar-blue")  #dolarhoy
    #os.system("start chrome https://bingx.com/es/CopyTrading/1093972264653701125")  #bingx
    #os.system("start chrome https://bingx.com/es/CopyTrading/1093972264653701125")  #bingx anti vitalik
    os.system("start chrome https://mdchi2.github.io/monitor/")  #monitor
    
    time.sleep(10)
    wifi('off')
    pausa(3600)  # pausa 1h=3600seg
    cerrarvent()
