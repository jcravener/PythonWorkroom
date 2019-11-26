


def palindrone(s):

    for leftidnex in range(len(s)//2):
        rightindex = len(s) - 1 - leftidnex

        print(s[leftidnex], ":", s[rightindex])


str = 'racecar'

palindrone(str)


