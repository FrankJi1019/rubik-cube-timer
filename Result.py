
class Result:

    NO_PUNISH = 0
    PLUS_TWO = 1
    DNF = 2

    def __init__(self, time, scramble, state):
        self.__time = round(time, 2)
        self.__scramble = scramble
        self.__state = state
        if state == Result.DNF:
            self.__strTime = "DNF"
        elif state == Result.PLUS_TWO:
            self.__strTime = str(self.__time) + "+"
        else:
            self.__strTime = str(self.__time)

    def getTime(self):
        return self.__time

    def getScramble(self):
        return self.__scramble

    def getState(self):
        return self.__state

    def setState(self, state):
        if state != self.__state:
            if state == Result.NO_PUNISH:
                self.__strTime = str(self.__time)
            elif state == Result.PLUS_TWO:
                self.__strTime = str(round(float(self.__time)+2, 2)) + "+"
            else:
                self.__strTime = "DNF"
            self.__state = state

    def __str__(self):
        return self.__strTime
