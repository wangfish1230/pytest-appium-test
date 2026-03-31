# Appium 快速参考

## 安装与启动

### 安装 Appium
```bash
npm install -g appium
appium driver install xcuitest   # iOS
appium driver install uiautomator2  # Android
```

### 启动 Appium 服务
```bash
appium
# 或指定端口
appium --port 4724
```

## 运行测试

```bash
# 安装依赖
poetry install

# 激活虚拟环境
poetry shell

# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_basic.py::TestAppiumBasics::test_app_launch

# 显示详细输出
pytest -vs

# 显示打印语句
pytest -s

# 生成 HTML 报告（需要 pytest-html）
pytest --html=report.html
```

## 常用导入

```python
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

## 元素定位

| 方式 | 代码 | 说明 |
|-----|------|------|
| ID | `AppiumBy.ID` | 元素 ID 属性 |
| XPath | `AppiumBy.XPATH` | XML 路径表达式 |
| Class Name | `AppiumBy.CLASS_NAME` | 元素类名 |
| Accessibility ID | `AppiumBy.ACCESSIBILITY_ID` | iOS: accessibility label |
| UiAutomator | `AppiumBy.ANDROID_UIAUTOMATOR` | Android native selector |
| iOS Predicate | `AppiumBy.IOS_PREDICATE` | iOS native selector |

## 常用操作

```python
# 元素交互
element.click()
element.send_keys("text")
element.clear()
text = element.text
attr = element.get_attribute("name")
element.is_displayed()
element.is_enabled()

# 查找元素
driver.find_element(AppiumBy.ID, "id")
driver.find_elements(AppiumBy.XPATH, "//Element")

# 屏幕操作
driver.swipe(x1, y1, x2, y2, duration=500)
driver.get_window_size()
driver.orientation  # 获取屏幕方向

# 等待
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((AppiumBy.ID, "id")))
wait.until(EC.visibility_of_element_located((AppiumBy.ID, "id")))
wait.until(EC.element_to_be_clickable((AppiumBy.ID, "id")))

# 隐式等待
driver.implicitly_wait(5)
```

## Android 特定定位

```python
# UiAutomator 定位
# 按文本查找
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiSelector().text("Login")')

# 按资源ID查找
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceId("com.example:id/button")')

# 按类型和索引查找
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.Button").index(0)')
```

## iOS 特定定位

```python
# Predicate 定位
driver.find_element(AppiumBy.IOS_PREDICATE,
    'value = "Login"')

driver.find_element(AppiumBy.IOS_PREDICATE,
    'type = "XCUIElementTypeButton" AND value = "Submit"')

# Accessibility ID（推荐）
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button")
```

## XPath 示例

```python
# 文本匹配
//android.widget.Button[@text='登录']
//XCUIElementTypeButton[@label='Login']

# 属性匹配
//android.widget.EditText[@resource-id='input_id']
//android.widget.TextView[@index='0']

# 包含文本
//*[contains(@text, '登')]

# 以...开头
//*[starts-with(@text, '登')]

# 组合条件
//android.widget.Button[@text='登录' and @enabled='true']

# 获取父元素
//android.widget.EditText/..

# 获取下一个兄弟元素
//android.widget.Button[@text='登录']/following-sibling::android.widget.Button
```

## Capabilities 常用参数

### Android
```python
{
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Android Emulator',
    'app': '/path/to/app.apk',  # 或使用 appPackage + appActivity
    'appPackage': 'com.example.app',
    'appActivity': '.MainActivity',
    'autoGrantPermissions': True,
    'noReset': False,
    'clearSystemFiles': False,
}
```

### iOS
```python
{
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 15',
    'udid': 'auto',  # 或具体的设备 UDID
    'bundleId': 'com.example.app',
    'app': '/path/to/app.app',
    'noReset': False,
}
```

## 调试技巧

### 使用 Appium Inspector
```bash
npm install -g appium-inspector
appium-inspector
```

### 获取页面源代码
```python
page_source = driver.page_source
print(page_source)
```

### 截图
```python
driver.save_screenshot('screenshot.png')
```

### 查看日志
```bash
appium -g /tmp/appium.log  # 生成日志文件
```

### ADB 命令（Android）
```bash
adb devices                      # 列出设备
adb shell dumpsys window hierarchy     # 获取页面结构
adb logcat                       # 查看系统日志
adb shell input tap x y          # 点击屏幕坐标 (x, y)
```

## Page Object Model 模板

```python
from appium.webdriver.common.appiumby import AppiumBy

class MyPage:
    # 元素定位
    BUTTON = (AppiumBy.ID, "com.example:id/button")
    INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_button(self):
        self.driver.find_element(*self.BUTTON).click()
    
    def enter_text(self, text):
        self.driver.find_element(*self.INPUT).send_keys(text)
```

## 常见错误排查

| 错误 | 原因 | 解决方案 |
|-----|------|--------|
| `ConnectionError` | Appium 服务未启动 | 启动 Appium: `appium` |
| `NoSuchElementException` | 找不到元素 | 检查定位器，使用 Inspector |
| `TimeoutException` | 等待超时 | 增加等待时间，检查元素是否存在 |
| `StaleElementReferenceException` | 元素已过期 | 重新查找元素 |
| `JSONDecodeError` | Appium 响应错误 | 检查服务器日志 |

---

更多信息参见 [README.md](README.md) 或 [Appium 官方文档](https://appium.io/docs/en/latest/)
