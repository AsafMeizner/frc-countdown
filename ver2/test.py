# imports \/
from ctypes import Structure, windll, c_uint, sizeof, byref #afktime imports
import time
import pyautogui
import webbrowser
import pystray
from PIL import Image, ImageDraw
from threading import Thread
import os

idle_triger = 0.1

def on_clicked(sorterTray,item):
    if str(item)=="idle threshold is " + str(idle_triger) + " minutes":
        # print("iam download path")
        pass
    elif str(item)=="plus 5 minutes":
        idle_triger = idle_triger + 5
    elif str(item)=="minus 5 minutes":
        idle_triger = idle_triger - 5
    elif str(item)=="Exit":
        sorterTray.stop()
        os._exit()

# get idle duration \/
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
def get_idle_duration():

    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image
# icon=create_image(64, 64, 'black', 'white')

# sorterTray=pystray.Icon("DownloadSorter",icon,menu=pystray.Menu(
#     pystray.MenuItem("idle threshold is " + str(idle_triger) + " minutes",on_clicked),
#     pystray.MenuItem("plus 5 minutes",on_clicked),
#     pystray.MenuItem("minus 5 minutes", on_clicked),
#     pystray.MenuItem("Exit",on_clicked)
# ))

def tray_lol():
    icon = Image.new('RGB', (64, 64), 255)
    dc = ImageDraw.Draw(icon)
    dc.rectangle(
        (64 // 2, 0, 64, 64 // 2),
        fill=0)
    dc.rectangle(
        (0, 64 // 2, 64 // 2, 64),
        fill=0)
    # icon=create_image(64, 64, 'black', 'white')

    sorterTray=pystray.Icon("DownloadSorter",icon,menu=pystray.Menu(
        pystray.MenuItem("idle threshold is " + str(idle_triger) + " minutes",on_clicked),
        pystray.MenuItem("plus 5 minutes",on_clicked),
        pystray.MenuItem("minus 5 minutes", on_clicked),
        pystray.MenuItem("Exit",on_clicked)
    ))
    sorterTray.run()

    
Thread1 = Thread(target=tray_lol)
Thread1.start()

while True:
    # print(get_idle_duration()) #print afktime
    if int(get_idle_duration()) >= 10: #if afktime is greater than 10 seconds
        print("You are idle")
        if open == False:
            webbrowser.open('https://www.tickcounter.com/countdown/3585314/frc-kickoff', new=2)
            time.sleep(0.5)
            pyautogui.press('f11')
            start_time = time.time()
            time.sleep(0.5)

            while time.time() - start_time < 10:
                print(time.time()-start_time)

                if get_idle_duration() <0.3:
                    break
        open = True
    elif get_idle_duration() < 10 and open == True:
        pyautogui.press('f11')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        open = False 
    else: 
        open = False