from threading import Thread

import keyboard  # using module keyboard
import time


class Automator(Thread):
    def __init__(self, t, action, stop, stop_args=None, action_args=None, extra=None, extra_args=None):
        super().__init__()
        self.__t = t
        self.__action = action
        self.__action_args = action_args
        self.__stop = stop
        self.__stop_args = stop_args
        self.__extra = extra
        self.__extra_args = extra_args
        self.__running = False
        self.__counter = 0

    def run(self):
        while True:
            if self.__running:
                self.__do()
                time.sleep(self.__t)
                if self.__running:
                    self.__undo()
                    self.__extra_step()
                    self.__counter += 1

    def toggle(self):
        if not self.__running:
            print(type(self).__name__ + " running!")
        else:
            self.__undo()
            print(type(self).__name__ + " ran " + str(self.__counter) + " times")
            self.__counter = 0
            print(type(self).__name__ + " paused")
        self.__running = not self.__running

    def __do(self):
        self.__action(*self.__action_args)

    def __undo(self,):
        self.__stop(*self.__stop_args)

    def __extra_step(self, *args):
        if self.__extra is not None:
            self.__extra(*self.__extra_args)
