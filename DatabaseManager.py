import pymysql

from Result import Result


class DatabaseManager:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                                          port=3306,
                                          user="root",
                                          password="root",
                                          database="python")
        self.cursor = self.connection.cursor()
        self.__countResult = 0

    def readPreviousData(self):
        sql = "SELECT * FROM cubing_timer"
        self.cursor.execute(sql)
        allSolves = self.cursor.fetchall()
        self.__countResult = len(allSolves)
        results = []
        for solve in allSolves:
            time = round(float(solve[0]), 2)
            state = int(solve[1])
            scramble = solve[2]
            r = Result(time, scramble, state)
            results.append(r)
        return results

    def writeToDB(self, results):
        for i in range(self.__countResult, len(results)):
            result = results[i]
            sql = "INSERT INTO cubing_timer (time, state, scramble, date) VALUES ({}, {}, \"{}\", NOW())".format(
                result.getTime(), result.getState(), result.getScramble())
            self.cursor.execute(sql)
            self.connection.commit()

    def disconnect(self):
        self.connection.close()
