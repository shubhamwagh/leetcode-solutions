class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        a = 0
        b = 0
        ans = []
        while a < len(A) and b < len(B):
            start, end = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            
            
            if start <=end:
                
                ans.append([start, end])
            
            if A[a][1] > B[b][1]:
                b+=1
            else:
                a+=1
        return ans