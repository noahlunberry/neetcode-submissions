class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)

        prefix_products[0] = nums[0]
        suffix_products[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i-1] * nums[i]    
        for i in range(len(nums) - 2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i]    
        
        na = [0] * len(nums)

        for index, value in enumerate(nums):
            if (index == 0):
                na[0] = suffix_products[1] 
            elif (index == len(nums) - 1):
                na[index] = prefix_products[len(nums) - 2]
            else:
                na[index] = prefix_products[index-1] * suffix_products[index+1]
        return na
        
