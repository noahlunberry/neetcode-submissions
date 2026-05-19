class Solution:
    def isValid(self, s: str) -> bool:

        openers = ['[' , '{', '(']
        closers = [']' , '}', ')']

        my_stack = []

        for char in s:
            if char in openers:
                my_stack.append(char)
            elif char in closers:
                if (len(my_stack) == 0):
                    return False
                top = my_stack[-1]
                if openers.index(top) == closers.index(char):
                    my_stack.pop()
                else:
                    return False
        if (len(my_stack) == 0):
            return True
        else: 
            return False
