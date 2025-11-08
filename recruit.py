import pyautogui
import pytesseract
from PIL import ImageGrab, ImageOps

# Configuration settings
pyautogui.PAUSE = .5
# Specify the path to tesseract executable (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Coordinates for OCR region (adjust these based on your screen)
OCR_REGION = (850, 560, 1200, 700)  # left, top, right, bottom

def clickImg(image, accurate=False):
    try:
        if accurate:
            location = pyautogui.locateOnScreen(image, confidence=.99, grayscale=True)
        else:
            location = pyautogui.locateOnScreen(image, confidence=.8, grayscale=True)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
        else:
            print(f"Image {image} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def matchImg(image):
    try:
        return pyautogui.locateOnScreen(image, confidence=.99, grayscale=True) is not None
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def matchImgWithCenters(image):
    try:
        matches = pyautogui.locateAllOnScreen(image, confidence=.9, grayscale=True)
        centers = []
        for match in matches:
            center = pyautogui.center(match)
            centers.append(center)
        return centers
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def filter_centers(centers, threshold=10):
    filtered_centers = []
    for center in centers:
        x, y = center
        if not any(abs(x - cx) <= threshold and abs(y - cy) <= threshold for cx, cy in filtered_centers):
            filtered_centers.append(center)
    return filtered_centers

def perform_ocr():
    """
    Perform OCR on the predefined screen region to extract numbers.
    Returns the extracted text as a string.
    """
    try:
        # Capture the specified screen region
        screenshot = ImageGrab.grab(bbox=OCR_REGION)
        
        # Image preprocessing: grayscale and thresholding
        gray_image = ImageOps.grayscale(screenshot)
        threshold = 128
        binary_image = gray_image.point(lambda p: p < threshold and 255)
        
        # Perform OCR with configuration to only recognize digits
        text = pytesseract.image_to_string(
            binary_image, 
            config='--psm 6 -c tessedit_char_whitelist=0123456789'
        )
        return text.strip()
    except Exception as e:
        print(f"OCR error occurred: {e}")
        return ""

def loopScript():
    clickImg('pictures/recruit/battle.png')
    clickImg('pictures/recruit/level.png')
    clickImg('pictures/recruit/start.png')
    clickImg('pictures/recruit/attack.png')
    pyautogui.sleep(1)
    
    centers = matchImgWithCenters('pictures/recruit/role.png')
    filtered_centers = filter_centers(centers)
    
    for center in filtered_centers:
        x, y = center
        pyautogui.click(x, y)
        
        # Perform OCR after clicking each role
        extracted_numbers = perform_ocr()
        print(f"Extracted numbers: {extracted_numbers}")
        try:
            if extracted_numbers and int(extracted_numbers) > 3800:  # Convert to int before comparison
                clickImg('pictures/recruit/buy.png')
        except ValueError:
            print(f"Could not convert '{extracted_numbers}' to a number")
        clickImg('pictures/recruit/close.png')
    
    clickImg('pictures/recruit/pause.png')
    clickImg('pictures/recruit/reset.png')
    clickImg('pictures/recruit/confirm.png')
while True:
    loopScript()