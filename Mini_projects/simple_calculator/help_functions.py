# The calculator evaluation function

# Sets used for conditions in the evaluation
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

def insert_into_stack(operator, number, stack):
    """Help function that evaluates an operator"""
    match operator:
        case "+":
            stack.append(int(number))
        case "-":
            stack.append(int(-number))
        case "*":
            result = stack.pop() * int(number)
            stack.append(result)
        case "/":
            result = int(stack.pop()) / int(number)
            stack.append(result)
            
# Use this "global" i
i = 0
def calculate(s):
    """The main eval function"""
    global i
    num = 0
    stack = []

    # Begin with current operator +
    cur_operator = "+"

    while i < len(s):
        cur_char = s[i]

        if cur_char in digits:
            # If the number is multiple digits, build it up
            num = num * 10 + int(cur_char)

        if cur_char not in digits or i == len(s) - 1:
            if cur_char == "(":
                i += 1
                num = calculate(s)
            
            if cur_char == ")":
                insert_into_stack(cur_operator, num, stack)
                break
            # Reset num to 0 when at the end of the operation
            insert_into_stack(cur_operator, num, stack)
            num = 0
            cur_operator = cur_char
        
        i += 1

    final_res = 0
    # Add all elements from the stack for the final answer.
    while stack:
        final_res += stack.pop()
    return final_res