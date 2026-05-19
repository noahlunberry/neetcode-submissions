class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}

        for letter in s:
            my_map[letter] = my_map.get(letter, 0) + 1

        for letter in t:
            if letter not in my_map:
                return False
            my_map[letter] = my_map[letter] - 1

            if my_map[letter] == 0:
                del my_map[letter]
            
        return not my_map