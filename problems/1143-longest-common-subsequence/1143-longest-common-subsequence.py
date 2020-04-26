class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0 for j in range(0, len(text2) + 1)] for i in range(0, len(text1) + 1)]
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    DP[i+1][j+1] = DP[i][j] + 1
                else:
                    DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])
        return DP[-1][-1]