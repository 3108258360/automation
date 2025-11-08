import pytesseract
from PIL import ImageGrab, ImageOps

# 指定 tesseract 可执行文件的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 指定要截取的屏幕区域的左上角和右下角坐标
left, top, right, bottom = 850, 560, 1200, 700

# 使用指定的坐标截取屏幕区域
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# 保存截取的屏幕区域图片
screenshot.save('screenshot.png')

# 图像预处理：灰度化
gray_image = ImageOps.grayscale(screenshot)

# 图像预处理：二值化
threshold = 128
binary_image = gray_image.point(lambda p: p < threshold and 255)

# 使用 pytesseract 进行 OCR，只识别数字，并调整 Tesseract 配置
text = pytesseract.image_to_string(binary_image, config='--psm 6 -c tessedit_char_whitelist=0123456789')

print(text)
