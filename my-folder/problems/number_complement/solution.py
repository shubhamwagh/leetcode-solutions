class Solution:
    def findComplement(self, num: int) -> int:
        
        
        # Use XOR with bit 1 and left shift that bit by 1 every iteration until original number is 0 
        
        bit =1
        temp = num
        
        while temp:
            num  = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num    
    
        # b_str = bin(num).replace('0b', '')
        # mask_str = ''.join(['1'] * len(b_str))
        # return num ^ int(mask_str, 2)