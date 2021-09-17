import os
import time

a = 0
while True:
    time.sleep(0.5)
    os.system("adb shell input tap 562 397")
    time.sleep(1)
    os.system("adb shell input tap 289 1287")
    time.sleep(15)
    a += 1  
    print(f"今天挂机{a}次")
