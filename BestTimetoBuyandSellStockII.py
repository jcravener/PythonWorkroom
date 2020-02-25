

# LeetCode: 122. Best Time to Buy and Sell Stock II

def maxProfit(prices: [int]) -> int:

    prof = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            prof += prices[i] - prices[i-1]
    
    return prof

i = [1,2,3,4,5]
i = [7,1,5,3,6,4]
i = [7,6,4,3,1]
print(maxProfit(i))