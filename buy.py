# 安装并导入Appium-Python-Client
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
# 定义设备和应用的配置参数
capabilities = dict(
    platformName='Android',            # 指定平台名称为 Android
    automationName='uiautomator2',     # 使用uiautomator2作为自动化引擎
    deviceName='Android',              # 设备名称，这里使用通用名称
    # 查看包名和Activity
    # adb shell dumpsys activity recents | findstr /i intent | Select-Object -First 1
    appPackage='com.wangwango.strategylegion2',      # 要测试的应用包名
    appActivity='.strategylegion',     # Activity名称
    noReset=True,                      # 不重置应用状态
    newCommandTimeout=60,              # 设置超时时间为60秒
)
# 创建一个远程WebDriver实例，连接到Appium服务器
driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
# 设置隐式等待时间，单位为秒
driver.implicitly_wait(10)
# 定义全局变量
buy = [(910, 160)]
confirm = [(650, 500)]
while True:
    driver.tap(buy)
    for i in range(2):
        driver.tap(confirm)

