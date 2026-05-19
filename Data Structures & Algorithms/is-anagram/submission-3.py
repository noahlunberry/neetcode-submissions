class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map1 = {}
        my_map2 = {}

        for letter in s:
            if letter in my_map1:
                my_map1[letter] += 1
            else:
                my_map1[letter] = 1
        
        for letter in t:
            if letter in my_map2:
                my_map2[letter] += 1
            else:
                my_map2[letter] = 1
                
        if my_map1 == my_map2:
            return True
        else:
            return False