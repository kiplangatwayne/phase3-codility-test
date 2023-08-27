def is_balanced(expression):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for exp in expression:
        if exp in '({[':
            stack.append(exp)
        elif exp in ')}]':
            if not stack or stack[-1] != brackets_map[exp]:
                return False
            stack.pop()

    return not stack

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2))  

