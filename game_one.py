import os
import time

a = 0
while True:
    time.sleep(0.5)
    os.system("adb shell input tap 545 2001")
    time.sleep(1)
    os.system("adb shell input tap 541 1813")
    time.sleep(15)
    os.system("adb shell input tap 527 2136")
    a += 1
    print(f"今天挂机{a}次")
