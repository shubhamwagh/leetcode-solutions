class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for ind in range(len(s)):
            count_s[s[ind]] = count_s.get(s[ind], 0) + 1
            count_t[t[ind]] = count_t.get(t[ind], 0) + 1

        for key in count_s:
            if count_s[key] != count_t.get(key, 0):
                return False
        return True