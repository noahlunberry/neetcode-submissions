class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        answer = []

        for index, num in enumerate(nums):
            if (index > 0) and (num == nums[index-1]):
                continue
            a = num
            b_location = index + 1
            c_location = len(nums) - 1
            last_added = []
            while b_location < c_location:
                b = nums[b_location]
                c = nums[c_location]
                total = a + b + c
                if (total == 0) and (last_added != [a, b, c]):
                    answer.append([a, b, c])
                    last_added = [a, b, c]
                    b_location += 1
                elif total > 0:
                    c_location -= 1
                elif total < 0:
                    b_location += 1
                else:
                    b_location += 1
        return answer

                    
                