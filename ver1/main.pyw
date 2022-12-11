from ctypes import Structure, windll, c_uint, sizeof, byref #afktime imports
import time
import pyautogui
import webbrowser

idle_threshold = 10

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


while True:
    print(get_idle_duration()) #print afktime
    if int(get_idle_duration()) >= idle_threshold * 60: #if afktime is greater than 10 seconds
        print("You are idle")
        if open == False:
            webbrowser.open('https://www.tickcounter.com/countdown/3585314/frc-kickoff', new=2)
            time.sleep(0.5)
            pyautogui.press('f11')
            start_time = time.time()
            time.sleep(0.5)

            while time.time() - start_time < idle_threshold * 60:
                print(time.time()-start_time)

                if get_idle_duration() <0.3:
                    break
        open = True
    elif get_idle_duration() < idle_threshold * 60 and open == True:
        pyautogui.press('f11')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        open = False 
    else: 
        open = False