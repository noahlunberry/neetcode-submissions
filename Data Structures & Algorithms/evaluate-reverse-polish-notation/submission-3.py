class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        main_stack = []

        for char in tokens:
            try:
                num = int(char)
                main_stack.append(num)
            except ValueError:

                first_operand = main_stack.pop()
                second_operand = main_stack.pop()
                if (char == '+'):
                    answer = first_operand + second_operand
                    main_stack.append(answer)
                if (char == '-'):
                    answer = second_operand - first_operand
                    main_stack.append(answer)
                if (char == '*'):
                    answer = first_operand * second_operand
                    main_stack.append(answer)                    
                if (char == '/'):
                    
                    answer = int(second_operand/first_operand)
                    main_stack.append(answer)


        return main_stack[-1]
            