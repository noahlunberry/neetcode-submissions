class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        words = {}
        for word in strs:
            sortedfd = sorted(word)
            sortedfdf = ''.join(sortedfd)
            if sortedfdf in words:
                words[sortedfdf].append(word)
            else:
                words[sortedfdf] = [word]
        
        mainList = list(words.values())
        return (mainList)
  

            
        