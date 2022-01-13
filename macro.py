import time
from pynput.mouse import Button, Controller
mouse = Controller()

print("get ready for speed")
time.sleep(2)
for i in range(100000):
        mouse.press(Button.left)
        mouse.release(Button.left)

