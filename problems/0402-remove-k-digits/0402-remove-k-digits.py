class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        count = k
        for val in num:
            while count and stack and stack[-1] > val:
                stack.pop()
                count -= 1
            stack.append(val)
        res = "".join(stack[0:len(num)-k]).lstrip("0")
        
        if len(res):
            return res
        else:
            return "0"