from Cube import Cube
from Result import Result
from Setting import *


def generateStatistics(results):
    totalTime = 0
    best = 1000
    worst = -1
    successfulSolve = 0
    for result in results:
        if result.getState() != Result.DNF:
            t = result.getTime() + (2 if result.getState() == Result.PLUS_TWO else 0)
            totalTime += t
            if best > t:
                best = t
            if worst < t:
                worst = t
            successfulSolve += 1
    average = ("%.2f" % (totalTime / successfulSolve)) if successfulSolve != 0 else "NA"
    best = ("%.2f" % best) if successfulSolve != 0 else "NA"
    worst = ("%.2f" % worst) if successfulSolve != 0 else "NA"
    totalSolve = len(results)
    return successfulSolve, totalSolve, best, worst, average


class MainScreen:
    def __init__(self):
        self.__window = pygame.display.set_mode(screenSize)
        self.__clock = pygame.time.Clock()
        self.__cube = Cube()

    def drawButton(self, location, size, text):
        pygame.draw.rect(self.__window, buttonColor, (location[0], location[1], size[0], size[1]))
        DisplayMessage(self.__window, text, (location[0]+size[0]/2, location[1]+size[1]/2), buttonTextColor, size[1])
        mousePos = pygame.mouse.get_pos()
        if location[0] < mousePos[0] < location[0]+size[0] and location[1] < mousePos[1] < location[1]+size[1]:
            mousePress = pygame.mouse.get_pressed()[0]
            pygame.draw.rect(self.__window, buttonColorHover, (location[0], location[1], size[0], size[1]))
            DisplayMessage(self.__window, text, (location[0] + size[0] / 2, location[1] + size[1] / 2),
                           buttonTextColorHover, size[1])
            if mousePress:
                return True
        return False

    def drawButton1(self, x, y, width, height, color1, color2, fontColor, text, fontSize):
        DisplayMessage(self.__window, text, (x+width/2, y+height/2), fontColor, fontSize)
        mousePos = pygame.mouse.get_pos()
        if x < mousePos[0] < x+width and y < mousePos[1] < y+height:
            color = color1
        else:
            color = color2
        pygame.draw.rect(self.__window, color, (x, y, width, height), 5)
        return x < mousePos[0] < x+width and y < mousePos[1] < y+height and pygame.mouse.get_pressed()[0]

    def drawButton2(self, x, y, width, height, color1, color2, color3, color4, text, fontSize):
        pygame.draw.rect(self.__window, color1, (x, y, width, height))
        DisplayMessage(self.__window, text, (x+width/2, y+height/2), color3, fontSize)
        mousePos = pygame.mouse.get_pos()
        if x < mousePos[0] < x+width and y < mousePos[1] < y+height:
            pygame.draw.rect(self.__window, color2, (x, y, width, height))
            DisplayMessage(self.__window, text, (x+width/2, y+height/2), color4, fontSize)
            return bool(pygame.mouse.get_pressed()[0])
        return False

    def display(self, results):
        self.__cube.fix()
        scramble, strScramble = self.__cube.generateScramble()
        self.__cube.disturb(scramble)
        successfulSolve, totalSolve, best, worst, average = generateStatistics(results)
        newScrambleGenerated = 0
        scrambleGenerationGap = 10
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return strScramble
            self.__window.fill(bgColor)

            # display the scramble algorithm
            DisplayMessage(self.__window, strScramble, (GetX(0.5), GetY(0.065)), scrambleColor, 30, "arial")

            # display the scramble pattern
            self.__cube.draw(self.__window, (GetX(0.75), GetY(0.65)), 60)

            # display last solve
            DisplayMessage(self.__window, results[-1] if len(results) != 0 else "0.00",
                           (GetX(0.5), GetY(0.4)), lastSolveColor, 150)

            # display the three buttons
            if self.drawButton1(GetX(0.4), GetY(0.68), 100, 50, buttonRectColorHover, buttonRectColor,
                                buttonRectTextColor, "DNF", 30) and len(results) != 0:
                results[-1].setState(Result.DNF)
                successfulSolve, totalSolve, best, worst, average = generateStatistics(results)
            if self.drawButton1(GetX(0.535), GetY(0.68), 100, 50, buttonRectColorHover, buttonRectColor,
                                buttonRectTextColor, "+2", 30) and len(results) != 0:
                results[-1].setState(Result.PLUS_TWO)
                successfulSolve, totalSolve, best, worst, average = generateStatistics(results)
            if self.drawButton1(GetX(0.4), GetY(0.82), 250, 50, buttonRectColorHover, buttonRectColor,
                                buttonRectTextColor, "No Punishment", 30) and len(results) != 0:
                results[-1].setState(Result.NO_PUNISH)
                successfulSolve, totalSolve, best, worst, average = generateStatistics(results)
            if self.drawButton2(GetX(0.82), GetY(0.11), 120, 50, buttonColor, buttonColorHover,
                                buttonTextColor, buttonTextColorHover, "update", 35) \
                    and not newScrambleGenerated:
                scramble, strScramble = self.__cube.generateScramble()
                newScrambleGenerated = 1
                self.__cube.fix()
                self.__cube.disturb(scramble)

            # display the statistics
            DisplayMessage(self.__window, str(successfulSolve)+"/"+str(totalSolve), (GetX(0.16), GetY(0.60)),
                           staticsFontColor, 30, 'arial')
            DisplayMessage(self.__window, "average solve: " + str(average), (GetX(0.16), GetY(0.70)),
                           staticsFontColor, 30, 'arial')
            DisplayMessage(self.__window, "best solve: " + str(best), (GetX(0.16), GetY(0.80)),
                           staticsFontColor, 30, 'arial')
            DisplayMessage(self.__window, "worst solve: " + str(worst), (GetX(0.16), GetY(0.90)),
                           staticsFontColor, 30, 'arial')

            newScrambleGenerated += int(bool(newScrambleGenerated))
            if newScrambleGenerated >= scrambleGenerationGap:
                newScrambleGenerated = 0
            pygame.display.update()
            self.__clock.tick(refreshTimes)
