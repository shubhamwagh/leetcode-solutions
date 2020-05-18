class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_len, s1_len = len(s2), len(s1)
        
        if s2_len < s1_len:
            return False
        
        s2_count = Counter()
        s1_count = Counter(s1)
        result = []
        for i in range(s2_len):
            s2_count[s2[i]]+=1
            
            if i>= s1_len:
                if s2_count[s2[i - s1_len]] ==1:
                    del s2_count[s2[i - s1_len]]
                else:
                    s2_count[s2[i - s1_len]] -=1
            if s2_count == s1_count:
                return True
        return False        
                    