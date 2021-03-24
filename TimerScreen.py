import time

from Result import *
from Setting import *


class TimerScreen:
    def __init__(self):
        self.__window = pygame.display.set_mode(screenSize)
        self.__clock = pygame.time.Clock()

    def display(self, scramble):
        startTime = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    result = Result(time.time()-startTime, scramble, Result.NO_PUNISH)
                    return result
            self.__window.fill(bgColor)

            currentTime = "%.2f" % (time.time() - startTime)
            DisplayMessage(self.__window, currentTime, (GetX(0.5), GetY(0.5)), timerColor, 300)

            pygame.display.update()
            self.__clock.tick(refreshTimes)
