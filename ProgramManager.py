from MainScreen import MainScreen
from ReadyScreen import ReadyScreen
from TimerScreen import TimerScreen
from DatabaseManager2 import DatabaseManager
from Setting import *


class ProgramManager:
    def __init__(self):
        self.__readyScreen = ReadyScreen()
        self.__timerScreen = TimerScreen()
        self.__mainScreen = MainScreen()
        self.__dbManager = DatabaseManager()

        self.__results = self.__dbManager.readPreviousData()

    def run(self):
        while True:
            scramble = self.__mainScreen.display(self.__results)
            if scramble == -1:
                break
            i = self.__readyScreen.display()
            if i == MAIN_SCREEN:
                continue
            else:
                result = self.__timerScreen.display(scramble)
                self.__results.append(result)
        self.update()
        self.end()

    def update(self):
        self.__dbManager.writeToDB(self.__results)

    def end(self):
        self.__dbManager.disconnect()
