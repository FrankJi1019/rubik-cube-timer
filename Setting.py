import pygame


screenSize = (1100, 650)
refreshTimes = 100
MAIN_SCREEN = 1
READY_SCREEN = 2
TIMER_SCREEN = 3

# colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
COLOR = [ORANGE, GREEN, RED, BLUE, WHITE, YELLOW]

# All Screens
bgColor = (255, 255, 255)
# MainScreen
scrambleColor = BLACK
lastSolveColor = BLACK
buttonColor = (200, 200, 200)
buttonColorHover = (0, 0, 200)
buttonTextColor = (0, 0, 200)
buttonTextColorHover = (100, 100, 100)
buttonRectColor = (50, 50, 50)
buttonRectColorHover = (255, 0, 0)
buttonRectTextColor = (0, 0, 0)
staticsFontColor = (0, 0, 0)
# ReadyScreen
readyColor1 = (0, 200, 200)
readyColor2 = (0, 255, 255)
# TimerScreen
timerColor = (50, 50, 50)


def GetX(percent):
    return round(percent * screenSize[0])


def GetY(percent):
    return round(percent * screenSize[1])


def DisplayMessage(gameWindow, text, center, color, fontSize, font="consolas"):
    text = str(text)
    textFont = pygame.font.SysFont(font, fontSize, True)
    textSurf = textFont.render(text, True, color)
    textRec = textSurf.get_rect()
    textRec.center = (center[0], center[1])
    gameWindow.blit(textSurf, textRec)
