# Appium 测试项目 - 快速开始指南

这是一个使用 **Appium + Pytest** 进行移动应用自动化测试的项目。

## 📋 前置要求

### 1. 安装必要的工具

#### macOS：
```bash
# 安装 Node.js（如果还没有）
brew install node

# 全局安装 Appium
npm install -g appium

# 安装 iOS 驱动
appium driver install xcuitest

# 安装 Android 驱动
appium driver install uiautomator2
```

#### Linux/Windows：
参考 [Appium 官方文档](https://appium.io/docs/en/2.1/quickstart/)

### 2. 配置开发环境

```bash
# 进入项目目录
cd pytest-appium-test

# 使用 Poetry 安装依赖
poetry install

# 激活虚拟环境
poetry shell
```

### 3. 准备测试设备

**Android：**
- 启动 Android 模拟器，或连接真实 Android 设备
- 使用 `adb devices` 验证设备连接
- 准备测试应用的 APK 文件

**iOS：**
- 在 Xcode 中启动 iOS 模拟器
- 或连接真实 iOS 设备
- 准备测试应用的 .app 或 .ipa 文件

## 🚀 快速开始

### 1. 启动 Appium 服务器

```bash
appium
```

默认监听：`http://localhost:4723`

### 2. 配置测试参数

编辑 [conftest.py](conftest.py) 中的 `capabilities` 字典：

**Android 示例：**
```python
capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Android Emulator',
    'app': '/path/to/your/app.apk',
    'appPackage': 'com.example.app',
    'appActivity': '.MainActivity',
}
```

**iOS 示例：**
```python
capabilities = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 15',
    'app': '/path/to/your/app.app',
    'bundleId': 'com.example.app',
}
```

### 3. 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_basic.py

# 运行特定测试用例
pytest tests/test_basic.py::TestAppiumBasics::test_app_launch

# 显示更详细的输出
pytest -v

# 显示打印语句
pytest -s

# 结合使用
pytest -vs tests/test_basic.py
```

## 📚 主要文件说明

### [conftest.py](conftest.py)
- Pytest 配置文件
- 定义 `driver` fixture，用于初始化和清理 WebDriver

### [tests/test_basic.py](tests/test_basic.py)
- 基础测试用例集合
- 演示常见的 Appium 操作：寻找元素、点击、输入文本等

### [config/capabilities.py](config/capabilities.py)
- 存储设备配置和 capabilities
- 支持 Android、iOS 和 Web 配置

## 🔍 常用的元素定位方法

| 定位方式 | 用法 | 支持情况 |
|--------|------|--------|
| ID | `AppiumBy.ID` | ✅ Android/iOS |
| XPath | `AppiumBy.XPATH` | ✅ Android/iOS |
| Class Name | `AppiumBy.CLASS_NAME` | ✅ Android/iOS |
| Accessibility ID | `AppiumBy.ACCESSIBILITY_ID` | ✅ iOS推荐 |
| Android UiAutomator | `AppiumBy.ANDROID_UIAUTOMATOR` | ✅ Android |
| iOS Predicate | `AppiumBy.IOS_PREDICATE` | ✅ iOS |

### 使用示例：

```python
from appium.webdriver.common.appiumby import AppiumBy

# 按 ID 查找
driver.find_element(AppiumBy.ID, "com.example:id/button")

# 按 XPath 查找
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='确认']")

# 按文本查找（iOS）
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login Button")

# Android UiAutomator
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
```

## 📱 常用 Appium 操作

```python
# 点击元素
element.click()

# 输入文本
element.send_keys("text")

# 清空输入框
element.clear()

# 获取文本
text = element.text

# 获取属性值
attr = element.get_attribute("attribute_name")

# 长按元素
from appium.webdriver.common.touch_action import TouchAction
action = TouchAction(driver)
action.long_press(element).perform()

# 滑动屏幕
driver.swipe(x1, y1, x2, y2, duration=500)

# 获取屏幕大小
size = driver.get_window_size()

# 等待元素出现
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "element_id")))

# 获取所有匹配的元素
elements = driver.find_elements(AppiumBy.XPATH, "//android.widget.Button")
```

## 🐛 常见问题

### 1. 连接超时
```
ConnectionError: Appium 服务器未运行
```
**解决方案：**
- 确保 Appium 服务器已启动（`appium` 命令）
- 检查 Appium 服务器地址和端口是否正确

### 2. 找不到设备
```
Error: 找不到可用的 Android 设备
```
**解决方案（Android）：**
```bash
# 列出所有连接的设备
adb devices

# 启动模拟器
emulator -avd emulator_name
```

### 3. 应用启动失败
- 检查应用路径是否正确
- 验证应用包名和启动活动是否正确
- 确保应用已安装或路径有效

### 4. 元素找不到
- 使用 Appium Inspector 工具检查元素
- 确保等待时间充分
- 尝试不同的定位方式

## 🔧 有用的工具

### Appium Inspector
图形化工具，用于检查应用元素和生成定位器。

```bash
npm install -g appium-inspector
appium-inspector
```

### Java 代码生成工具
```bash
# 查看页面结构
adb shell dumpsys window hierarchy
```

## 📖 更多资源

- [Appium 官方文档](https://appium.io/docs/en/latest/)
- [Pytest 文档](https://docs.pytest.org/)
- [Selenium WebDriver API](https://www.selenium.dev/documentation/)

## 💡 最佳实践

1. **使用 Page Object Model (POM)** - 分离页面逻辑和测试代码
2. **显式等待** - 用 WebDriverWait 代替隐式等待
3. **清晰的测试命名** - 测试名称应能自我解释
4. **独立的测试用例** - 每个测试应该独立运行
5. **适当的错误处理** - 使用 try/except 处理可能的异常

---

祝您测试顺利！🎉
