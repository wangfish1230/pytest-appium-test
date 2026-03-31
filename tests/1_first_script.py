from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "Android"

# ⚠️ 改成你的 APK 路徑
options.app = "/Users/cherry.cy.wang/Desktop/ApiDemos-release.apk"
# ✅ 改成 ApiDemos 的
options.app_package = "io.appium.android.apis"
options.app_activity = ".ApiDemos"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

sleep(3)

driver.quit()