
# LeetCode: 1029. Two City Scheduling

def twoCitySchedCost(costs: [[int]]) -> int:

    mid = len(costs)//2
    
    costs.sort(key=lambda c: c[1] - c[0])
    for i in range(len(costs)): print(costs[i], costs[i][1] - costs[i][0])
    print()
    print(sum([i[0] for i in costs[:mid]]) + sum([i[1] for i in costs[mid:]]))
    print()

    #-- THE KEY HERE is to sort the list by the diff of: elemen[0] - element[1]
    costs.sort(key=lambda c: c[0] - c[1])
    for i in range(len(costs)): print(costs[i], costs[i][0] - costs[i][1])
    print()

    return sum([i[0] for i in costs[:mid]]) + sum([i[1] for i in costs[mid:]])



a = [[10,20],[30,200],[400,50],[30,20]]

print(twoCitySchedCost(a))
