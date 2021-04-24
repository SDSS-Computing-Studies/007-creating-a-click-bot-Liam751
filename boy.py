import pyautogui
import time

a = 1

def main():
    while a <= 10: 
        curTime = time.time()
        first()
        second(a)
        print("aaa")

def first():
    pyautogui.click(611, 397)
    pyautogui.click(519, 416)

def second(a):
    pyautogui.click(846, 333)


main()



