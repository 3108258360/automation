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
battle = [(1100, 640)]
# level = [(600, 350)] # 35关
# level = [(80, 490)]  # 73关
level = [(1080, 490)]# 89关
start = [(650, 510)]
attack = [(70, 560)]
pause=[(30, 30)]
restart=[(350, 300)]
confirm=[(470, 300)]
while True:
    time.sleep(.2)
    driver.tap(battle)
    time.sleep(.2)
    driver.tap(level)
    time.sleep(.2)
    driver.tap(start)
    for i in range(14):
        driver.tap(attack)
        if i == 13:
            driver.tap(pause)
            driver.tap(restart)
            driver.tap(confirm)
        time.sleep(.5)
# 关闭会话
# driver.quit()

# def click_on_template(driver, template_path):
#     global level  # 声明使用全局变量 level
#     # 获取并解码屏幕截图
#     screenshot_data = np.frombuffer(base64.b64decode(driver.get_screenshot_as_base64()), np.uint8)
#     screen = cv2.imdecode(screenshot_data, cv2.IMREAD_COLOR)
#     # 读取目标图像
#     template = cv2.imread(template_path)
#     # 模板匹配
#     result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
#     _, max_val, _, max_loc = cv2.minMaxLoc(result)
#     # 计算目标图像中心点的坐标
#     h, w = template.shape[:2]
#     center_x = max_loc[0] + w // 2
#     center_y = max_loc[1] + h // 2
#     # 将坐标写入 level 变量
#     level = [(center_x, center_y)]
#     # 点击目标图像中心点
#     driver.tap([(center_x, center_y)])
# # 示例调用
# click_on_template(driver, 'level.png')