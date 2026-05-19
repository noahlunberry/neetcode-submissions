import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_list = defaultdict(int)
        bucket_array = [[] for i in range(len(nums)+1)]

        for num in nums:
            my_list[num] += 1
        
        for key, value in my_list.items():
            bucket_array[value].append(key)

        return_list = []
        for i in range(len(bucket_array) - 1, 0, -1):
            for num in bucket_array[i]:
                return_list.append(num)
                if (len(return_list) == k):
                    return return_list
                

