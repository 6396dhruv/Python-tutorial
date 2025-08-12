import pyautogui
import time
import pyperclip

# Small delay before running so you can switch to the target app
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1285, 1421)
time.sleep(1)  # wait for app/window to open

# Step 2: Drag to select text
pyautogui.moveTo(822, 395)
pyautogui.dragTo(2095, 1242, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get clipboard content
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)
