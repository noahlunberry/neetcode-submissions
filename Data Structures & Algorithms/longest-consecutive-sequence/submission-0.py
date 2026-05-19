class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_list = defaultdict(int)

        for num in nums:
            my_list[num] += 1
        
        longest = 0


        for num in nums:
            # start of sequence (number before it doesn't exist)
            if ((num-1) not in my_list):
                array = [num]
                while (array[-1] + 1) in my_list:
                    array.append(array[-1] + 1)
                if len(array) > longest:
                    longest = len(array)
            else:
                continue
        return longest