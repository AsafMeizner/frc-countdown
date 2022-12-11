from threading import Thread
import time
import os
import sys
from PySide2 import QtWidgets, QtGui
from ctypes import Structure, windll, c_uint, sizeof, byref #afktime imports
import pyautogui
import webbrowser

idle_triggre = 0.1

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

def loop_function():
    print(get_idle_duration()) #print afktime
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

def thread_loop():
    while True:
        loop_function() # executing every minute

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Wallpy')
        menu = QtWidgets.QMenu(parent)

        time_dfsdfs = menu.addAction("idle threshold is " + str(idle_triggre) + " minutes")

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)


def tray():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("C:/Users/ASAFM/OneDrive/Desktop/countdown/ver2/myicon.png"), w)
    tray_icon.show()
    app.exec_()

my_loop = Thread(target=thread_loop, args=()) # Start the thread with no args
my_loop.start()
tray() # launch tray icon