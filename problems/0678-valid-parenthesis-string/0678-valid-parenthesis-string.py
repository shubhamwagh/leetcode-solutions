class Solution:
    def checkValidString(self, s: str) -> bool:

        
        if s == "":
            return True
        
        paranthesis_stack = []
        star_stack = []
        
        for ind in range(0, len(s)):
            if s[ind] == "(":
                paranthesis_stack.append(ind)
            
            elif s[ind] == "*":
                star_stack.append(ind)
            
            elif s[ind] == ")":
                if len(paranthesis_stack) !=0:
                    paranthesis_stack.pop()
                
                elif len(paranthesis_stack) ==0 and len(star_stack)!=0:
                    star_stack.pop()
                
                elif len(paranthesis_stack) ==0 and len(star_stack) ==0:
                    return False
        
        while len(paranthesis_stack) !=0 and len(star_stack)!=0:
            popped_ind = star_stack.pop()
            if paranthesis_stack[-1] < popped_ind:
                paranthesis_stack.pop()
        
        return len(paranthesis_stack) == 0 

#         if s == "" or s == "*":
#             return True
#         if len(s) < 2:
#             return False
        
#         left = 0
#         for i in s:
#             if i == ")":
#                 left-=1
#             else:
#                 left+=1
#             if left < 0:
#                 return False
#         if left ==0 :
#             return True
        
#         right = 0
#         for i in reversed(s):
#             if i =="(":
#                 right-=1
#             else:
#                 right+=1
#             if right < 0:
#                 return False
#         return True