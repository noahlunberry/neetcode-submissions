class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        test = [2, 1, 1, 3]
        answer = [3, 2, 1, 0]

        answer = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and ((stack[-1][0]) < temp):
                popped = stack.pop()
                answer[popped[1]] = index - popped[1]
            stack.append((temp, index))
        return answer