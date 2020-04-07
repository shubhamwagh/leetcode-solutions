class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        if arr==None or len(arr)==0:
            return 0
        count = 0
        
        # for i in range(0, len(arr)):
        #     count_set = set()
        #     for j in range(0, len(arr)):
        #         current = arr[i]
        #         if i!=j and arr[i] + 1 == arr[j] and arr[j] not in count_set:
        #             count_set.add(arr[j])
        #             count+=1
        # return count            
        
        count_dict = {}
        for val in arr:
            count_dict[val] = 1    
        count = 0
        for val in arr:
            if val + 1 in count_dict:
                count+=1
        return count