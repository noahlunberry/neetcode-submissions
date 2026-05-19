class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0) and (i != j) and (j != k) and (i != k):
                        x = [nums[i], nums[j], nums[k]]
                        x.sort()
                        if x not in answer:
                            answer.append(x)
        return answer