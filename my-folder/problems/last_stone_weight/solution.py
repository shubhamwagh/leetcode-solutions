class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        while len(stones)!=1:
            stones.sort()
            y = stones.pop(-1)
            x = stones.pop(-1)
            
            diff = y -x
            if diff ==0:
                if len(stones) !=0:
                    continue
                elif len(stones) == 0:
                    return diff
            elif diff!=0:
                stones.append(diff)
        return stones[-1]        
            