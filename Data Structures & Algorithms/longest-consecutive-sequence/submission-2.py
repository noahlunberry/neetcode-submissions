class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_list = defaultdict(int)

        for num in nums:
            my_list[num] += 0
        
        longest = 0


        for num in my_list:
            # start of sequence (number before it doesn't exist)
            if ((num-1) not in my_list):
                current = num
                length = 1
                while (current + 1) in my_list:
                    current += 1
                    length += 1
                if length > longest:
                    longest = length
                    my_list[num] += 1
            else:
                continue
        return longest