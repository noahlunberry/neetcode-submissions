class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        pairs = sorted(zip(position, speed), reverse=True)


        my_stack = []

        for car in pairs:
            time = (target - car[0]) / car[1]
            if (len(my_stack) == 0) or (my_stack[-1] < time) :
                my_stack.append(time)
        return len(my_stack)