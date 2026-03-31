"""
Appium 双语快速入门指南 (Quick Start Guide)
"""

# ============================================================================
# 一、项目结构 (Project Structure)
# ============================================================================

PROJECT_STRUCTURE = """
pytest-appium-test/
├── conftest.py                  # Pytest 配置和 driver fixture
├── pytest.ini                   # Pytest 配置文件
├── pyproject.toml               # Poetry 项目配置
├── README.md                    # 详细文档
├── QUICK_REFERENCE.md           # 快速参考手册
├── config/
│   ├── __init__.py
│   └── capabilities.py          # 设备配置 (Android/iOS/Web)
├── tests/
│   ├── __init__.py
│   ├── test_basic.py            # 基础测试示例
│   ├── test_advanced.py         # POM 高级测试示例
│   └── pages/
│       ├── __init__.py
│       ├── base_page.py         # Page Object 基类
│       └── login_page.py        # 登录页面示例
"""

# ============================================================================
# 二、快速开始 (Quick Start)
# ============================================================================

QUICK_START = """
1. 安装依赖
   $ npm install -g appium
   $ appium driver install xcuitest        # iOS
   $ appium driver install uiautomator2    # Android
   $ poetry install

2. 启动 Appium 服务
   $ appium

3. 配置 conftest.py 中的 capabilities (修改设备信息)

4. 运行测试
   $ poetry shell
   $ pytest -vs
"""

# ============================================================================
# 三、关键文件说明 (Key Files)
# ============================================================================

KEY_FILES = {
    "conftest.py": "定义 driver fixture，自动初始化和清理 WebDriver",
    "tests/test_basic.py": "核心测试示例，演示元素定位和基本操作",
    "tests/test_advanced.py": "高级示例，展示 Page Object Model 模式",
    "tests/pages/base_page.py": "Page Object 的基类，包含常用方法",
    "config/capabilities.py": "存储 Android/iOS 的设备配置参数",
    "README.md": "完整的项目文档和教程",
    "QUICK_REFERENCE.md": "快速参考手册",
}

# ============================================================================
# 四、常用命令 (Common Commands)
# ============================================================================

COMMANDS = {
    "启动 Appium": "appium",
    "启动特定端口": "appium --port 4724",
    "运行所有测试": "pytest",
    "运行特定文件": "pytest tests/test_basic.py",
    "运行特定用例": "pytest tests/test_basic.py::TestAppiumBasics::test_app_launch",
    "显示详细输出": "pytest -v",
    "显示打印信息": "pytest -s",
    "结合使用": "pytest -vs tests/test_basic.py",
}

# ============================================================================
# 五、Capabilities 配置示例 (Capabilities Examples)
# ============================================================================

ANDROID_CAPABILITIES = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Android Emulator',
    # 方案 A: 使用本地 APK
    'app': '/path/to/app.apk',
    # 方案 B: 使用应用包名和启动活动（应用已安装）
    # 'appPackage': 'com.example.app',
    # 'appActivity': '.MainActivity',
    'autoGrantPermissions': True,
}

IOS_CAPABILITIES = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 15',
    'udid': 'auto',  # 自动选择可用设备
    'bundleId': 'com.example.app',
    'app': '/path/to/app.app',
}

# ============================================================================
# 六、元素定位 (Element Locators)
# ============================================================================

LOCATORS = """
from appium.webdriver.common.appiumby import AppiumBy

# 按 ID
driver.find_element(AppiumBy.ID, "id_value")

# 按 XPath
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Save']")

# 按文本 (Android)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiSelector().text("Login")')

# 按 Accessibility ID (iOS)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button")

# 按 iOS Predicate
driver.find_element(AppiumBy.IOS_PREDICATE, 
    'type = "XCUIElementTypeButton" AND label = "Submit"')
"""

# ============================================================================
# 七、常用操作 (Common Operations)
# ============================================================================

OPERATIONS = {
    "点击": "element.click()",
    "输入文本": "element.send_keys('text')",
    "清空": "element.clear()",
    "获取文本": "text = element.text",
    "获取属性": "attr = element.get_attribute('name')",
    "滑动": "driver.swipe(x1, y1, x2, y2, duration=500)",
    "等待（示例）": """
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(
    (AppiumBy.ID, "element_id")
))
""",
}

# ============================================================================
# 八、调试工具 (Debugging Tools)
# ============================================================================

DEBUG_TOOLS = {
    "Appium Inspector": {
        "安装": "npm install -g appium-inspector",
        "启动": "appium-inspector",
        "用途": "图形化工具，检查应用元素和获取定位器",
    },
    "ADB 命令（Android）": {
        "列出设备": "adb devices",
        "获取页面结构": "adb shell dumpsys window hierarchy",
        "查看日志": "adb logcat",
        "点击坐标": "adb shell input tap x y",
    },
}

# ============================================================================
# 九、最佳实践 (Best Practices)
# ============================================================================

BEST_PRACTICES = [
    "✓ 使用 Page Object Model - 分离页面逻辑和测试代码",
    "✓ 使用显式等待 - 用 WebDriverWait 代替隐式等待",
    "✓ 清晰的测试名称 - 测试名称应能自我解释",
    "✓ 独立的测试 - 每个测试应能独立运行",
    "✓ 错误处理 - 使用 try/except 处理异常",
    "✓ 使用 Fixtures - 利用 @pytest.fixture 管理测试资源",
    "✓ 参数化测试 - 使用 @pytest.mark.parametrize 进行数据驱动测试",
]

# ============================================================================
# 十、常见问题 (FAQ)
# ============================================================================

FAQ = {
    "Q: 找不到元素?": [
        "1. 使用 Appium Inspector 验证元素是否存在",
        "2. 检查定位器是否正确",
        "3. 使用显式等待来确保元素加载完成",
        "4. 尝试不同的定位方法",
    ],
    "Q: ConnectionError - Appium 服务未运行?": [
        "1. 启动 Appium 服务: appium",
        "2. 检查地址和端口是否正确: http://localhost:4723",
        "3. 查看 Appium 服务器日志",
    ],
    "Q: 设备找不到?": [
        "Android: adb devices 查看设备列表",
        "iOS: 在 Xcode 中启动模拟器",
        "检查驱动是否已安装",
    ],
}

if __name__ == "__main__":
    print("Appium 项目结构")
    print(PROJECT_STRUCTURE)
    print("\nQuick Start")
    print(QUICK_START)
