from threading import Thread

import keyboard  # using module keyboard
import win32api
import win32con
import time


class Click(Thread):
    def __init__(self, t, x=0, y=0):
        super().__init__()
        self.__t = t
        self.__x = x
        self.__y = y
        self.__running = False
        self.__counter = 0

    def run(self):
        while True:
            if self.__running:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.__x, self.__y, 0, 0)
                time.sleep(self.__t)
                if self.__running:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.__x, self.__y, 0, 0)
                    self.__counter += 1

    def toggle(self):
        if not self.__running:
            print("Clicker running!")
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.__x, self.__y, 0, 0)
            print("Clicker ran " + str(self.__counter) + " times")
            self.__counter = 0
            print("Clicker paused")
        self.__running = not self.__running
