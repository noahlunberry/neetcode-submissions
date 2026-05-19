class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        


        my_list = {}

        for index, num in enumerate(numbers):
            other_target = target - num 

            if other_target in my_list:
                return [my_list[other_target] + 1, index + 1]
            else:
                my_list[num] = index