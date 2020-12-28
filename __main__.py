
import keyboard  # using module keyboard

from Click import Click
from Press import Press

if __name__ == '__main__':
    clicker = Click(.85)
    presser = Press(.85, 'z')
    keyboard.add_hotkey('f6', clicker.toggle)
    keyboard.add_hotkey('f7', presser.toggle)
    clicker.start()
    presser.start()
    print("Ready to go!")
    while True:
        continue
