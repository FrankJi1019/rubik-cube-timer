import numpy
import random

from Setting import *


class Cube:
    def __init__(self):
        self.cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],  # green = 0
                     [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # red = 1
                     [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # blue = 2
                     [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # orange = 3
                     [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # white = 4
                     [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]  # yellow = 5
        self.cube = numpy.array(self.cube)
        self.lengthOfScramble = 25

    def generateScramble(self):
        moves = ['R', 'L', 'U', 'D', 'B', 'F']
        counter = 0
        scramble = []
        while counter < self.lengthOfScramble:
            move = random.choice(moves)
            while len(scramble) != 0 and (moves.index(move) // 2) == (moves.index(scramble[-1][0]) // 2):
                move = random.choice(moves)
            double = True if random.randint(0, 3) == 0 else False
            if double:
                move = move + "2"
            else:
                move = move + ("'" if random.choice([True, False]) else "")
            scramble.append(move)
            counter += 1
        strScramble = ""
        for m in scramble:
            strScramble += (m + " ")
        return scramble, strScramble

    def disturb(self, scramble):
        for move in scramble:
            repeat = 2 if move[-1] == '2' else (3 if move[-1] == "'" else 1)
            if move[0] == 'R':
                for i in range(repeat):
                    self.__R()
            if move[0] == 'L':
                for i in range(repeat):
                    self.__L()
            if move[0] == 'U':
                for i in range(repeat):
                    self.__U()
            if move[0] == 'D':
                for i in range(repeat):
                    self.__D()
            if move[0] == 'F':
                for i in range(repeat):
                    self.__F()
            if move[0] == 'B':
                for i in range(repeat):
                    self.__B()

    def draw(self, window, location, size):
        def drawSquare(X, Y, squareColor):
            pygame.draw.rect(window, squareColor, (X, Y, squareSize, squareSize))

        def drawLine(x1, y1, x2, y2, width):
            pygame.draw.line(window, BLACK, (x1, y1), (x2, y2), width)

        squareSize = round(size / 3)
        squareSep = round(squareSize / 15)
        sideSep = round(squareSep * 1.5)
        x = location[0]
        y = location[1] + round(size)
        for i in range(4):
            startX = x + i * 3 * squareSize
            startY = y
            for j in range(3):
                for g in range(3):
                    color = COLOR[self.cube[i][g][j]]
                    drawSquare(startX + (j + 0) * squareSize, startY + (g + 0) * squareSize, color)
        for i in [4, 5]:
            startX = x + 3 * squareSize
            startY = y + (3 * squareSize) * (-1 if i == 4 else 1)
            for j in range(3):
                for g in range(3):
                    color = COLOR[self.cube[i][g][j]]
                    drawSquare(startX + (j + 0) * squareSize, startY + (g + 0) * squareSize, color)
        # side lines
        drawLine(x + 12 * squareSize, y, x + 12 * squareSize, y + 3 * squareSize, sideSep)
        drawLine(x, y, x, y + 3 * squareSize, sideSep)
        drawLine(x, y, x + 12 * squareSize, y, sideSep)
        drawLine(x, y + 3 * squareSize, x + 12 * squareSize, y + 3 * squareSize, sideSep)
        drawLine(x + squareSize * 3, y - squareSize * 3, x + squareSize * 6, y - squareSize * 3, sideSep)
        drawLine(x + squareSize * 3, y + squareSize * 6, x + squareSize * 6, y + squareSize * 6, sideSep)
        drawLine(x + squareSize * 3, y - squareSize * 3, x + squareSize * 3, y + squareSize * 6, sideSep)
        drawLine(x + squareSize * 6, y - squareSize * 3, x + squareSize * 6, y + squareSize * 6, sideSep)
        drawLine(x + squareSize * 9, y, x + squareSize * 9, y + squareSize * 3, sideSep)
        # square lines
        for i in range(12):
            drawLine(x + i * squareSize, y, x + i * squareSize, y + 3 * squareSize, squareSep)
        for i in range(3):
            drawLine(x, y + i * squareSize, x + 12 * squareSize, y + i * squareSize, squareSep)
        for i in range(9):
            drawLine(x + 3 * squareSize, y - 3 * squareSize + i * squareSize, x + 6 * squareSize,
                     y - 3 * squareSize + i * squareSize, squareSep)
        drawLine(x + 4 * squareSize, y - 3 * squareSize, x + 4 * squareSize, y + 6 * squareSize, squareSep)
        drawLine(x + 5 * squareSize, y - 3 * squareSize, x + 5 * squareSize, y + 6 * squareSize, squareSep)

    def fix(self):
        self.cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],  # orange side
                     [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # green side
                     [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # red side
                     [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # blue side
                     [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # white side
                     [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]  # yellow side
        self.cube = numpy.array(self.cube)

    def move(self, m):
        if m == "R":
            self.__R()
        elif m == "L":
            self.__L()
        elif m == "U":
            self.__U()
        elif m == "D":
            self.__D()
        elif m == "B":
            self.__B()
        elif m == "F":
            self.__F()

    def __R(self):
        self.cube[2] = numpy.rot90(self.cube[2])
        self.cube[2] = numpy.rot90(self.cube[2])
        self.cube[2] = numpy.rot90(self.cube[2])
        temp = [self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2]]
        self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2] = \
            self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2]
        self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2] = \
            self.cube[3][2][0], self.cube[3][1][0], self.cube[3][0][0]
        self.cube[3][2][0], self.cube[3][1][0], self.cube[3][0][0] = \
            self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2]
        self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2] = temp[0], temp[1], temp[2]

    def __L(self):
        self.cube[0] = numpy.rot90(self.cube[0])
        self.cube[0] = numpy.rot90(self.cube[0])
        self.cube[0] = numpy.rot90(self.cube[0])
        temp = [self.cube[1][0][0], self.cube[1][1][0], self.cube[1][2][0]]
        self.cube[1][0][0], self.cube[1][1][0], self.cube[1][2][0] = \
            self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0]
        self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0] = \
            self.cube[3][2][2], self.cube[3][1][2], self.cube[3][0][2]
        self.cube[3][2][2], self.cube[3][1][2], self.cube[3][0][2] = \
            self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0]
        self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0] = temp[0], temp[1], temp[2]

    def __U(self):
        self.cube[4] = numpy.rot90(self.cube[4])
        self.cube[4] = numpy.rot90(self.cube[4])
        self.cube[4] = numpy.rot90(self.cube[4])
        temp = [self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2]]
        self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2] = \
            self.cube[1][0][0], self.cube[1][0][1], self.cube[1][0][2]
        self.cube[1][0][0], self.cube[1][0][1], self.cube[1][0][2] = \
            self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2]
        self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2] = \
            self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2]
        self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2] = \
            temp[0], temp[1], temp[2]

    def __D(self):
        self.cube[5] = numpy.rot90(self.cube[5])
        self.cube[5] = numpy.rot90(self.cube[5])
        self.cube[5] = numpy.rot90(self.cube[5])
        temp = [self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2]]
        self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2] = \
            self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2]
        self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2] = \
            self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2]
        self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2] = \
            self.cube[1][2][0], self.cube[1][2][1], self.cube[1][2][2]
        self.cube[1][2][0], self.cube[1][2][1], self.cube[1][2][2] = \
            temp[0], temp[1], temp[2]

    def __F(self):
        self.cube[1] = numpy.rot90(self.cube[1])
        self.cube[1] = numpy.rot90(self.cube[1])
        self.cube[1] = numpy.rot90(self.cube[1])
        temp = [self.cube[4][2][0], self.cube[4][2][1], self.cube[4][2][2]]
        self.cube[4][2] = [self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2]]
        self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2] = \
            self.cube[5][0][2], self.cube[5][0][1], self.cube[5][0][0]
        self.cube[5][0][2], self.cube[5][0][1], self.cube[5][0][0] = \
            self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0]
        self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0] = temp[0], temp[1], temp[2]

    def __B(self):
        self.cube[3] = numpy.rot90(self.cube[3])
        self.cube[3] = numpy.rot90(self.cube[3])
        self.cube[3] = numpy.rot90(self.cube[3])
        temp = [self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2]]
        self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2] = \
            self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2]
        self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2] = \
            self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0]
        self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0] = \
            self.cube[0][2][0], self.cube[0][1][0], self.cube[0][0][0]
        self.cube[0][2][0], self.cube[0][1][0], self.cube[0][0][0] = temp[0], temp[1], temp[2]
