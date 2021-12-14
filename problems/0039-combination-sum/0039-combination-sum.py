class Solution: 
    
    def combinationSumMemoise(self, candidates: List[int], target: int, memo: Dict = {}) -> List[List[int]]:
        if target in memo:
            return memo[target]
        
        all_combinations = []
        
        if target == 0:
            return [[]]
        
        if target < 0:
            return []
        
        for num in candidates:
            rem = target - num
            rem_res = self.combinationSumMemoise(candidates, rem, memo)
            
            for gl in rem_res:
                new_l = [num] + gl
                new_l.sort()
                if new_l not in all_combinations:
                    all_combinations.append(new_l)
        
        memo[target] = all_combinations
        return all_combinations
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumMemoise(candidates, target, {})