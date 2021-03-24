import sqlite3
import time

from Result import Result


class DatabaseManager:
    def __init__(self):
        self.__connection = sqlite3.connect("CubingTimer.db")
        self.__cursor = self.__connection.cursor()
        self.__countResult = 0

    def readPreviousData(self):
        sql = "SELECT * FROM cubing_timer"
        self.__cursor.execute(sql)
        allSolves = self.__cursor.fetchall()
        self.__countResult = len(allSolves)
        results = []
        for solve in allSolves:
            resultTime = round(float(solve[0]), 2)
            state = int(solve[1])
            scramble = solve[2]
            r = Result(resultTime, scramble, state)
            results.append(r)
        return results

    def writeToDB(self, results):
        date = time.strftime("%Y-%m-%d", time.localtime())
        for i in range(self.__countResult, len(results)):
            result = results[i]
            sql = "INSERT INTO cubing_timer (time, state, scramble, date) VALUES ({}, {}, \"{}\", {})".format(
                result.getTime(), result.getState(), result.getScramble(), date)
            self.__cursor.execute(sql)
            self.__connection.commit()

    def disconnect(self):
        self.__connection.close()
