from Setting import *


class ReadyScreen:
    def __init__(self):
        self.__window = pygame.display.set_mode(screenSize)
        self.__clock = pygame.time.Clock()
        self.__text = "READY"

    def display(self):
        timer = 0
        timeToGo = refreshTimes * 0.25
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and timer >= timeToGo:
                        return TIMER_SCREEN
                    if event.key == pygame.K_SPACE and timer < timeToGo:
                        return MAIN_SCREEN
            self.__window.fill(bgColor)

            # def DisplayMessage(gameWindow, text, center, color, fontSize, font="consolas")
            if timer < timeToGo:
                DisplayMessage(self.__window, self.__text, (GetX(0.5), GetY(0.5)), readyColor1, 300)
            else:
                DisplayMessage(self.__window, self.__text, (GetX(0.5), GetY(0.5)), readyColor2, 300)

            timer += 1

            pygame.display.update()
            self.__clock.tick(refreshTimes)
