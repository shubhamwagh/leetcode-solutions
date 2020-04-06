class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == None or len(strs) ==0:
            return [] 
        
        anagram_dict = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_dict: 
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        return anagram_dict.values()    
                        
                            
                    
        
        