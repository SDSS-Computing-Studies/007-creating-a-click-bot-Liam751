import pyautogui
import time

a = 0

def main(a):
    while a < 12: 
        curTime = time.time()
        first()
        second(a)
        third(a)
        fourth(a)
        fith(a)
        sixth(a)
        seventh(a)
        eighth(a)
        a = a + 1
        if a > 10:
            break

def first():
    #turn on auto
    pyautogui.click(624, 396)
    pyautogui.click(603, 418)

def second(a):
    #buy book
    time.sleep(240 - (10*a))
    pyautogui.click(941, 337)
    pyautogui.click(853, 801)

def third(a):
    #buy tent
    time.sleep(120 - (10*a))
    pyautogui.click(841, 488)

def fourth(a):
    #upgrade to military
    time.sleep(180 - (10*a))
    pyautogui.click(755, 337)
    pyautogui.click(829, 580)

def fith(a):
    #turn off bargaining
    time.sleep(101 - (10*a))
    pyautogui.click(844, 340)
    pyautogui.click(1456, 507)

def sixth(a):
    #buy dumbells
    time.sleep(120 - (10*a))
    pyautogui.click(940, 338)
    pyautogui.click(820, 545)

def seventh(a):
    #buy cottage
    time.sleep(180 - (10*a))
    pyautogui.click(936, 342)
    pyautogui.click(832, 589)

def eighth(a):
    #restart
    time.sleep(1500 - (60*a))
    pyautogui.click(1031, 341)
    pyautogui.click(822, 721)

main(1)
pyautogui.alert