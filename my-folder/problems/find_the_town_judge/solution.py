class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if len(trust) < N -1:
            return -1
        
        trust_arr = [0] * (N + 1)
        
        for i in range(0, len(trust)):
            trusting, trusted = trust[i]
            trust_arr[trusting] -=1
            trust_arr[trusted] +=1
        for i, score in enumerate(trust_arr[1:], 1):
            if score == N -1:
                return i
        return -1    