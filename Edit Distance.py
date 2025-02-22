class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n)
        #where, m and n are the lengths of word2 and word1, respectively
        
        m = len(word2)
        n = len(word1)
        
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        #first row
        for j in range(n + 1):
            dp[0][j] = j
        
        #first col
        for i in range(m + 1):
            dp[i][0] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]