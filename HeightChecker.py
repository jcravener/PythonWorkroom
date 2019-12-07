


def heightChecker(heights: [int]):
    
    heights_sorted = sorted(heights)

    count = 0

    for i in range(len(heights)):
        if heights[i] != heights_sorted[i]:
            count += 1

    return count

l = [1,1,4,2,1,3]
print(heightChecker(l))



