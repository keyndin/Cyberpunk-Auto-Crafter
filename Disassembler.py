from threading import Thread

import keyboard  # using module keyboard
import time

from Automator import Automator


class Disassembler(Automator):
    def __init__(self, delay=.85, key='z', confirm='tab'):
        super().__init__(
            delay,
            action=keyboard.press,
            action_args=(key,),
            stop=keyboard.release,
            stop_args=(key,),
            extra=keyboard.press_and_release,
            extra_args=(confirm,)
        )
