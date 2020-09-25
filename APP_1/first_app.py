# 打开安卓5.1.1设备上的app
# 启动参数 安卓6以上用UIAutomation2
desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "haha",
    "noReset": "true",
    # "fullReset":""
    # app - 包名 - 唯一标识 - 入口页面名称 activity名
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomActivity"
}
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By

# 1.与appium建立连接  2.告诉appium要干嘛
# 前提 1.保证设备是连接状态 adb devices 可用 2.appium server是启动状态
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((MobileBy.ID,"")))
ele = driver.find_element_by_id("")
ele.click()
driver.close_app()
driver.quit()

