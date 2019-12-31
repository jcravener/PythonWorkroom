

class Solution:
    def __init__(self):
        self
    
    def dayOfTheWeek(self, day: int, month: int, year: int):
        firstyear = 1971
        lastyear = 2100
        
        if year < firstyear or year > lastyear:
            return None

        r = ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday",]

        dtotal = 365
        ldtotal = 366
        totaldays = 0
        remainder = self.__yearday(day,month,year)

        for y in range(firstyear, year):
            if self.__isLeapYear(y):
                totaldays += ldtotal
            else:
                totaldays += dtotal
        
        totaldays += remainder

        return r[totaldays%7]
    
    def __isLeapYear(self, year: int):
        if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
            return True
        else:
            return False
    
    def __yearday(self, day: int, month: int, year: int):
        m = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        lm = [i for i in m]
        lm[2] = 29

        mnth = []

        if self.__isLeapYear(year):
            mnth = lm
        else:
            mnth = m
        
        mnth[month] = day
        return sum(mnth[:month+1])-1


s = Solution()
d = 1
m = 1
y = 2011

for y in range(y,y+11):
    print(y, s.dayOfTheWeek(d,m,y))

