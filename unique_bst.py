class Solution:
    # @return an integer
    def numTrees(self, n):
        DP = [0] * (n+1)
        DP[0] = 1
        for i in range(1,n+1):
            sum = 0
            for j in range(0,i):
                sum += DP[j] * DP[i-j-1]
            DP[i] = sum
        return DP[n]