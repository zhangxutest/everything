from appium import webdriver
import time

caps = {"platformName": "Android", "platformVersion": "10", "deviceName": "PWH4C19716006893",
        "appPackage": "com.ss.android.ugc.aweme", "appActivity": ".splash.SplashActivity",
        "resetKeyboard": True, "unicodeKeyboard": True}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
l = driver.get_window_size()
x1 = l['width'] * 0.75
y1 = l['height'] * 0.75
y2 = l['height'] * 0.25
x2 = l['width'] * 0.25
driver.implicitly_wait(20)
el1 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/a_w")
el1.click()
el2 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_deny_button")
el3.click()
while True:
    driver.swipe(x1, y1, x2, y2)
    time.sleep(3)
