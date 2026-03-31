"""
Pytest 配置文件 - 定义 Appium 驱动器的 fixtures
"""
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="function")
def driver():
    """
    初始化 Appium WebDriver
    
    修改 capabilities 根据您的测试需求：
    - platformName: 'iOS' 或 'Android'
    - deviceName: 设备名称
    - app: 应用包路径或 Bundle ID
    - automationName: 'XCUITest' (iOS) 或 'UiAutomator2' (Android)
    """
    
    # 基础配置
    capabilities = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'Android Emulator',
        'app': '/path/to/your/app.apk',  # 替换为您的应用路径
        'appPackage': 'com.example.app',  # 应用包名
        'appActivity': '.MainActivity',    # 启动活动
    }
    
    options = AppiumOptions()
    options.load_capabilities(capabilities)
    
    # 连接到 Appium 服务器 (默认: localhost:4723)
    appium_driver = webdriver.Remote(
        command_executor='http://localhost:4723',
        options=options
    )
    
    yield appium_driver
    
    # 清理 - 关闭应用
    if appium_driver:
        appium_driver.quit()
