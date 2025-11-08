import pyautogui
pyautogui.PAUSE = .5
def clickImg(image,accurate=False):
  try:
    if accurate:
      location = pyautogui.locateOnScreen(image,confidence=.99,grayscale=True)
    else:
      location = pyautogui.locateOnScreen(image,confidence=.8,grayscale=True)
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)
  except pyautogui.ImageNotFoundException:
    pyautogui.sleep(.5)
def matchImg(image):
  try:
    pyautogui.locateOnScreen(image,confidence=.99,grayscale=True)
    return True
  except pyautogui.ImageNotFoundException:
    return False
loop = True
def loopScript():
  global loop
  loop = True
  clickImg('pictures/loop/battle.png')
  clickImg('pictures/loop/level.png')
  clickImg('pictures/loop/start.png')
  while loop: 
    clickImg('pictures/loop/attack.png')
    if matchImg('pictures/loop/continue.png'):
      loop = False
      clickImg('pictures/loop/continue.png')
      loopScript()
      pyautogui.sleep(.5)
loopScript()