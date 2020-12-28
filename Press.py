from threading import Thread

import keyboard  # using module keyboard
import time


class Press(Thread):
    def __init__(self, t, key):
        super().__init__()
        self.__t = t
        self.key = key
        self.__running = False
        self.__counter = 0

    def run(self):
        while True:
            if self.__running:
                keyboard.press(self.key)
                time.sleep(self.__t)
                if self.__running:
                    keyboard.release(self.key)
                    keyboard.press_and_release('tab')
                    self.__counter += 1

    def toggle(self):
        if not self.__running:
            print("Presser running!")
        else:
            keyboard.release(self.key)
            print("Presser ran " + str(self.__counter) + " times")
            self.__counter = 0
            print("Presser paused")
        self.__running = not self.__running
