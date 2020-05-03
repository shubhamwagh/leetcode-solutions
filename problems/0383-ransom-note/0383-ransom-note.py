class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        

        m_dict = {}
        for val in magazine:
            if val in m_dict:
                m_dict[val] += 1
            else: m_dict[val] = 1
        
        
        for val in ransomNote:
            
            if val not in m_dict:
                return False
            
            if m_dict[val] <=0:
                return False
            
            m_dict[val] -=1
            
        return True