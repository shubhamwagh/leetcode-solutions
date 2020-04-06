class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = start= 0
        word_dict = {}
        if len(s) == 0:
            return 0
        
        for ind in range(0, len(s)):
            if s[ind] in word_dict and start <= word_dict[s[ind]]:
                start = word_dict[s[ind]] + 1
            else:
                max_length = max(max_length, ind - start + 1)
            word_dict[s[ind]]  = ind
        return max_length