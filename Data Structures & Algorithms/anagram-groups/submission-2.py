class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        my_list = {}
        for word in strs:
           #alphabet = [abcdefghijklmnopqrstuvwxyz] 
            alphabet = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                alphabet[index] += 1
            key = tuple(alphabet)
            if key in my_list:
                my_list[key].append(word) 
            else:
                my_list[key] = [word] 

        mainList = list(my_list.values())
        return mainList          
                
  

            
        