class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        ind = 0
        while ind < len(arr) - 1:
            if arr[ind] == 0:
                arr.insert(ind + 1, 0)
                del arr[len(arr) - 1]
                ind += 2
            else:
                ind += 1