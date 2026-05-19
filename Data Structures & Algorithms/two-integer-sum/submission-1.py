class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_map = {}

        for index, num in enumerate(nums):
            poop = target - num
            if poop in my_map:
                return [my_map[poop], index]
            my_map[num] = index
