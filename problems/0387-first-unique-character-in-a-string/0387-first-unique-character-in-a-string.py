class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for char in s:
            if char in map:
                map[char] +=1
            else:
                map[char] = 1

        for ind, char in enumerate(s):
            if map[char] == 1:
                return ind
        return -1