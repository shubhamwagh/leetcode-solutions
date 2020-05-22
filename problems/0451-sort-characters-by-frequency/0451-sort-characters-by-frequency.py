class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        result = ''
        for val in s:
            if val in map:
                map[val] +=1
            else:
                map[val] = 1
        
        s = sorted(map, key=lambda x: map[x], reverse=True)
        
        for val in s:
            result+= val * map[val]
        return result