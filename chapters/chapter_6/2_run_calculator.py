from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

# ==============================
# 1️⃣ 建立設定物件（告訴 Appium 要怎麼連線）
# ==============================
options = UiAutomator2Options()

# 指定平台：Android（固定寫法）
options.platform_name = "Android"

# 裝置名稱（可以隨便寫，Appium 不會真的用這個辨識）
options.device_name = "Android"

# ==============================
# 2️⃣ 指定要開啟的 App（計算機）
# ==============================

# app_package = App 的「唯一識別名稱」
# 就像 App 的 ID（例如：com.google.android.calculator）
options.app_package = "com.google.android.calculator"

# app_activity = App 啟動時的「入口畫面」
# 就像 main()，App 開啟會從這裡開始
options.app_activity = "com.android.calculator2.Calculator"

# ⚠️ 注意：
# 如果這兩個寫錯 → App 會開不起來

# ==============================
# 3️⃣ 建立與 Appium Server 的連線
# ==============================

# 這行會做：
# Python → 連線到 Appium → 控制 Android
driver = webdriver.Remote(
    "http://127.0.0.1:4723",  # Appium Server 位址（本機）
    options=options           # 上面設定的參數
)

# ==============================
# 4️⃣ 測試動作（這裡先簡單等待）
# ==============================

# 等待 3 秒（讓你看到 App 被打開）
sleep(3)

# ==============================
# 5️⃣ 結束測試
# ==============================

# 關閉 App + 結束 session
driver.quit()

# ==============================
# 🎯 整體流程總結
# ==============================
# 1. 設定裝置與 App
# 2. 連線 Appium Server
# 3. 開啟 App
# 4. 等待觀察
# 5. 關閉 App