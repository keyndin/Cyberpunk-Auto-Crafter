from threading import Thread

import keyboard  # using module keyboard
import win32api
import win32con
import time

from Automator import Automator


class Crafter(Automator):
    def __init__(self, delay=.85, x=0, y=0):
        super().__init__(
            delay,
            action=win32api.mouse_event,
            action_args=(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0),
            stop=win32api.mouse_event,
            stop_args=(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        )
