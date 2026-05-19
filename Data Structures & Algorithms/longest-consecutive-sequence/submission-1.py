class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_list = defaultdict(int)

        for num in nums:
            my_list[num] += 1
        
        longest = 0
        used_start = []


        for num in nums:
            # start of sequence (number before it doesn't exist)
            if ((num-1) not in my_list) and (num not in used_start):
                array = [num]
                while (array[-1] + 1) in my_list:
                    array.append(array[-1] + 1)
                if len(array) > longest:
                    longest = len(array)
                    used_start.append(array[0])
            else:
                continue
        return longest