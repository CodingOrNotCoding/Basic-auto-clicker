import keyboard
import pyautogui

while 1:
	if keyboard.is_pressed('b'):
		print('b Key was pressed')
		while 1:
			if keyboard.is_pressed('a'):
				pyautogui.alert('Program stopped')
				break
			pyautogui.click()

