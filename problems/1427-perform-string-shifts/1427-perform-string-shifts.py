# class Solution:
#     def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
#         string_list = list(s)
        
#         for operation in shift:
#             if operation[0] == 0:
                
#                 for i in range(0,operation[1]):
#                     val = string_list.pop(0)
#                     string_list.append(val)
                   
                    
#             elif operation[0] == 1:
                
#                 for i in range(0, operation[1]):
#                     val = string_list.pop(-1)
#                     temp_list = string_list[::-1]
#                     temp_list.append(val)
#                     string_list = temp_list[::-1]
#         return ''.join(string_list)
    
    
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        chars = collections.deque(s)
        for d, amount in shift:
            if d == 0:
                for _ in range(amount):
                    num = chars.popleft()
                    chars.append(num)
            else:
                for _ in range(amount):
                    num = chars.pop()
                    chars.appendleft(num)
        return ''.join(chars)