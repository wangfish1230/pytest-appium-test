# ============================================================
# 匯入標準函式庫
# subprocess: 用來在 Python 內執行 adb shell 指令
# unittest:   Python 內建測試框架，提供 TestCase、assert 等工具
# time:       提供 sleep()，讓操作之間有緩衝等待時間
# ============================================================
import subprocess
import unittest
import time

# ============================================================
# 匯入 Appium 相關模組
# webdriver:          建立與 Appium Server 的 RemoteDriver 連線
# UiAutomator2Options: Android 專用的 Capability 設定物件，
#                      對應 UIAutomator2 Driver（Google 官方推薦的 Android 自動化引擎）
# ============================================================
from appium import webdriver
from appium.options.android import UiAutomator2Options


class TestBasicOperations(unittest.TestCase):
    """
    示範 Appium 對 Android 裝置的基本操作：
    取得裝置資訊、截圖、鎖定/解鎖、按鍵模擬、App 資訊、旋轉、網路狀態、螢幕尺寸。
    """

    # ── 前置作業：建立 Driver 連線 ────────────────────────────────
    @classmethod
    def setUpClass(cls):
        """
        setUpClass 在整個測試類別執行前只會呼叫一次。
        使用 @classmethod 搭配 cls 是為了讓所有 test_* 方法共用同一個 driver，
        避免每個測試都重新啟動 App（耗時且無必要）。
        """
        # 建立 UiAutomator2 的 Capability 設定物件
        options = UiAutomator2Options()

        # 指定目標平台為 Android
        options.platform_name = 'Android'

        # app_package: 要啟動的 App 套件名稱（等同於 App 的唯一 ID）
        # 此處使用 Android 內建的「設定」App
        options.app_package = 'com.android.settings'

        # app_activity: App 的進入點 Activity，點號開頭表示省略 package 前綴
        options.app_activity = '.Settings'

        # 連線到本機的 Appium Server（預設 port 4723），並套用上方 Capability 設定
        # webdriver.Remote 會向 Appium Server 建立新的 Session
        cls.driver = webdriver.Remote('http://localhost:4723', options=options)

        # 設定隱式等待 10 秒：找元素時若未立即出現，最多等 10 秒再拋出例外
        cls.driver.implicitly_wait(10)

    # ── 後置清理：結束 Session ────────────────────────────────────
    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass 在整個測試類別執行完畢後只會呼叫一次。
        quit() 會關閉 App 並終止與 Appium Server 的 Session，釋放裝置資源。
        """
        cls.driver.quit()

    # ── 1. 取得裝置基本資訊 ──────────────────────────────────────
    def test_01_get_device_info(self):
        """
        driver.device_time: 回傳裝置當前時間（ISO 8601 格式字串）
        driver.orientation: 回傳目前螢幕方向，值為 'PORTRAIT' 或 'LANDSCAPE'
        """
        print(f"\n裝置時間: {self.driver.device_time}")
        print(f"畫面方向: {self.driver.orientation}")

        # 驗證 device_time 不為 None，確認裝置連線正常並能回應查詢
        self.assertIsNotNone(self.driver.device_time)

    # ── 2. 螢幕截圖 ──────────────────────────────────────────────
    def test_02_screenshot(self):
        """
        save_screenshot(path): 將目前畫面截圖並儲存為 PNG 檔案。
        路徑為相對於執行腳本的工作目錄，此處會存在專案根目錄下。
        常用於測試失敗時留存畫面證據。
        """
        self.driver.save_screenshot('./screenshot_ch6_7.png')
        print("\n截圖已儲存：screenshot_ch6_7.png")

    # ── 3. 鎖定與解鎖螢幕 ────────────────────────────────────────
    def test_03_lock_unlock(self):
        """
        driver.lock():      模擬按下電源鍵，將螢幕鎖定（黑屏）
        driver.unlock():    解鎖螢幕（滑動或無密碼直接解鎖）
        driver.is_locked(): 回傳 bool，True 表示目前處於鎖定狀態

        sleep(2): 鎖定後給予裝置足夠時間完成黑屏動畫，再驗證狀態
        sleep(1): 解鎖後等待畫面恢復，再驗證
        """
        self.driver.lock()
        time.sleep(2)
        print(f"\n是否鎖定: {self.driver.is_locked()}")
        self.assertTrue(self.driver.is_locked())

        self.driver.unlock()
        time.sleep(1)
        print(f"解鎖後是否鎖定: {self.driver.is_locked()}")
        self.assertFalse(self.driver.is_locked())

    # ── 4. 按下實體按鍵 (KeyCode) ────────────────────────────────
    def test_04_press_keycode(self):
        """
        press_keycode(code): 模擬按下 Android 實體或虛擬按鍵。
        KeyCode 是 Android 定義的整數常數，完整清單可參考：
        https://developer.android.com/reference/android/view/KeyEvent

        常用 KeyCode：
          3  = KEYCODE_HOME       → 回到主畫面（Launcher）
          4  = KEYCODE_BACK       → 返回上一頁
          24 = KEYCODE_VOLUME_UP  → 調高音量
          25 = KEYCODE_VOLUME_DOWN→ 調低音量
          26 = KEYCODE_POWER      → 電源鍵
        """
        self.driver.press_keycode(3)   # 回主畫面
        time.sleep(1)

        self.driver.press_keycode(4)   # 返回
        time.sleep(1)

        self.driver.press_keycode(24)  # 音量+
        time.sleep(1)
        print("\n按鍵操作完成")

    # ── 5. 取得目前 App 資訊 ─────────────────────────────────────
    def test_05_current_app_info(self):
        """
        current_package:  回傳目前前景 App 的 package 名稱（字串）
        current_activity: 回傳目前前景 App 的 Activity 名稱（字串）

        執行到此步驟時，因 test_04 按下 Home 鍵，前景 App 已切換為 Launcher，
        所以回傳值會是 Launcher 的 package，而非一開始的 com.android.settings。
        """
        current_app = self.driver.current_package
        current_activity = self.driver.current_activity
        print(f"\n目前 Package: {current_app}")
        print(f"目前 Activity: {current_activity}")
        self.assertIsNotNone(current_app)

    # ── 6. 旋轉螢幕方向 ──────────────────────────────────────────
    def test_06_orientation(self):
        """
        driver.orientation = 'LANDSCAPE'/'PORTRAIT': 切換螢幕方向。

        模擬器特殊問題說明：
        - Appium 的 orientation API 底層透過 UiAutomator 模擬感應器訊號，
          但 Android 模擬器沒有真實加速度計，會導致 2000ms timeout 錯誤。
        - Nexus Launcher 在 AndroidManifest 中宣告 screenOrientation=portrait，
          即使設定 accelerometer_rotation=1，Launcher 仍會強制鎖回直向。

        解決方案：改用 adb wm 指令直接操控 Window Manager：
        1. fixed-to-user-rotation enabled：忽略 App 層級的方向限制，
           強制以 user_rotation 設定為準
        2. user-rotation lock 1：鎖定為橫向（ROTATION_90）
        3. user-rotation lock 0：鎖定為直向（ROTATION_0）
        4. fixed-to-user-rotation default：測試完畢後還原，避免影響後續操作
        """
        # Step 1: 覆蓋 App 層級的方向限制（針對模擬器 Launcher 強制直向的問題）
        subprocess.run(['adb', 'shell', 'wm', 'fixed-to-user-rotation', 'enabled'])

        # Step 2: 將 Window Manager 鎖定為橫向（1 = ROTATION_90）
        subprocess.run(['adb', 'shell', 'wm', 'user-rotation', 'lock', '1'])
        time.sleep(1)  # 等待旋轉動畫完成後再讀取方向值

        self.assertEqual(self.driver.orientation, 'LANDSCAPE')
        print(f"\n橫向模式: {self.driver.orientation}")

        # Step 3: 切回直向（0 = ROTATION_0）
        subprocess.run(['adb', 'shell', 'wm', 'user-rotation', 'lock', '0'])
        time.sleep(1)

        self.assertEqual(self.driver.orientation, 'PORTRAIT')
        print(f"直向模式: {self.driver.orientation}")

        # Step 4: 還原旋轉策略，避免影響後續測試
        subprocess.run(['adb', 'shell', 'wm', 'fixed-to-user-rotation', 'default'])

    # ── 7. 網路狀態控制 ──────────────────────────────────────────
    def test_07_network(self):
        """
        driver.network_connection: 回傳整數，代表目前網路連線模式。
        數值是各網路類型 bit flag 的組合：
          0 = 無連線
          1 = 飛航模式（Airplane Mode）
          2 = Wi-Fi 開啟
          4 = 行動數據開啟
          6 = Wi-Fi + 行動數據（2 + 4）

        注意：set_network_connection(value) 可以用來切換模式，
        但部分模擬器對飛航模式切換有限制。
        """
        network_status = self.driver.network_connection
        print(f"\n目前網路狀態代碼: {network_status}")
        self.assertIsNotNone(network_status)

    # ── 8. 取得螢幕大小 ──────────────────────────────────────────
    def test_08_screen_size(self):
        """
        get_window_size(): 回傳字典 {'width': int, 'height': int}，
        代表裝置螢幕的實際像素尺寸（非 dp）。
        可用來計算滑動座標、元素相對位置等，在不同解析度裝置上做自適應定位。
        """
        size = self.driver.get_window_size()
        print(f"\n螢幕大小: 寬={size['width']}, 高={size['height']}")

        # 驗證回傳的字典包含 width 與 height 欄位
        self.assertIn('width', size)
        self.assertIn('height', size)


if __name__ == '__main__':
    # verbosity=2: 印出每個測試方法名稱與結果（ok / FAIL / ERROR），方便逐一確認
    unittest.main(verbosity=2)
