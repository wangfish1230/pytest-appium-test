"""
Appium 设备配置文件
支持 iOS 和 Android 的不同设备配置
"""


class AndroidConfig:
    """Android 设备配置"""
    
    # 基础配置
    PLATFORM_NAME = "Android"
    AUTOMATION_NAME = "UiAutomator2"
    DEVICE_NAME = "Android Emulator"
    
    # 应用配置
    APP_PACKAGE = "com.example.app"
    APP_ACTIVITY = ".MainActivity"
    # APP_PATH = "/path/to/app.apk"  # 本地应用路径
    
    # Appium 服务器
    APPIUM_SERVER = "http://localhost:4723"
    
    # 其他选项
    CAPABILITIES = {
        'platformName': PLATFORM_NAME,
        'automationName': AUTOMATION_NAME,
        'deviceName': DEVICE_NAME,
        'appPackage': APP_PACKAGE,
        'appActivity': APP_ACTIVITY,
        'noReset': False,         # 每次测试前重置应用
        'autoGrantPermissions': True,  # 自动授予权限
    }


class IOSConfig:
    """iOS 设备配置"""
    
    # 基础配置
    PLATFORM_NAME = "iOS"
    AUTOMATION_NAME = "XCUITest"
    DEVICE_NAME = "iPhone 15"
    OS_VERSION = "17.0"
    
    # 应用配置
    APP_BUNDLE_ID = "com.example.app"
    # APP_PATH = "/path/to/app.app"  # 本地应用路径
    
    # Appium 服务器
    APPIUM_SERVER = "http://localhost:4723"
    
    # 其他选项
    CAPABILITIES = {
        'platformName': PLATFORM_NAME,
        'automationName': AUTOMATION_NAME,
        'deviceName': DEVICE_NAME,
        'udid': 'auto',  # 自动选择可用设备
        'bundleId': APP_BUNDLE_ID,
        'noReset': False,
    }


class WebConfig:
    """Web 应用配置（通过浏览器打开的应用）"""
    
    # 基础配置
    PLATFORM_NAME = "Android"
    AUTOMATION_NAME = "UiAutomator2"
    DEVICE_NAME = "Android Emulator"
    
    # 浏览器配置
    BROWSER_NAME = "Chrome"
    
    # 应用配置
    APP_URL = "https://example.com"
    
    # Appium 服务器
    APPIUM_SERVER = "http://localhost:4723"
    
    CAPABILITIES = {
        'platformName': PLATFORM_NAME,
        'automationName': AUTOMATION_NAME,
        'deviceName': DEVICE_NAME,
        'browserName': BROWSER_NAME,
    }
