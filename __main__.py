
import keyboard  # using module keyboard

from Crafter import Crafter
from Disassembler import Disassembler

if __name__ == '__main__':
    clicker = Crafter(delay=.85)
    presser = Disassembler(delay=.85, key='z', confirm='tab')
    keyboard.add_hotkey('f6', clicker.toggle)
    keyboard.add_hotkey('f7', presser.toggle)
    clicker.start()
    presser.start()
    print("Ready to go!")
    while True:
        continue
