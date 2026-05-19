class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        best_capacity = 0

        while left < right:
            maxG = min(heights[right], heights[left]) * (right - left) 
            if maxG>best_capacity:
                best_capacity = maxG

            
            if heights[right] > heights[left]:
                left += 1
            
            elif heights[right] < heights[left]:
                right -= 1

            elif heights[right] == heights[left]:
                right -= 1
            
        return best_capacity

