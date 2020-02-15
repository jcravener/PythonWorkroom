
# LeetCode: 1137. N-th Tribonacci Number

dp = {}

def tribonacci(n: int) -> int:

    rt = 0

    if n == 0:
        return 0
    elif 0 < n <= 2:
        return 1
    else:
        rt =  tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        #if n in dp:
        #    rt =  dp[n]
        #else:
        #    dp[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        #    rt = dp[n]
    return rt

for n in range(26):
    print(tribonacci(n))

