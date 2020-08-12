import pyautogui
import time

time.sleep(5)

myScreenshot = pyautogui.screenshot()
myScreenshot.save('test.png')


for i in range(20):
	pyautogui.keyDown('shift')
	if i<5:
		pyautogui.keyDown('w')
	elif i<10:
		pyautogui.keyUp('w')
		pyautogui.keyDown('s')
	elif i<15:
		pyautogui.keyUp('s')
		pyautogui.keyDown('d')
	elif i<20:
		pyautogui.keyUp('w')
		pyautogui.keyDown('s')
		
pyautogui.keyUp('s')
pyautogui.keyDown('shift')
	