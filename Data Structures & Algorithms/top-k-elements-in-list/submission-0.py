class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_list = defaultdict(int)

        for num in nums:
            my_list[num] += 1
        

        k_most = []
        for i in range (k):

            value = max(my_list, key=my_list.get)


            k_most.append(value)
            del my_list[value]

        return(k_most)