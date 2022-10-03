class Time:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def gethours(self):
        return self.h

    def getmins(self):
        return self.m

    def getsecs(self):
        return self.s

    def tostring(self):
        return str(self.h) + ":" + str(self.m) + ":" + str(self.s)

    def timeinseconds(self):
        hours = self.h * 3600
        mins = self.m * 60
        return hours + mins + self.s

    def changethetime(self, hours, mins, secs):
        self.h = hours
        self.m = mins
        self.s = secs

    def twelvehourclock(self):
        if self.h > 12: # if hours is greater then 12 its night and to get hours you need to subtract 12
            return str(self.h) + ":" + str(self.m) + ":" + str(self.s) + "pm"
        else:
            str(self.h) + ":" + str(self.m) + ":" + str(self.s) + "am"

    def whattimeisit(self):
        if self.h <= 12 and self.h >= 6: # if it follows the parameters for morning it returns morning
            return "morning"
        elif self.h == 12 or self.h >= 1 and self.h <= 5:
            return "aternoon"
        elif self.h >= 5 and self.h <=10:
            return "evening"
        else:
            return "nighttime"

    def compareto(self, t):
        timedifference = t.timeinseconds()
        timedifference2 = self.timeinseconds()
        return timedifference2 - timedifference
