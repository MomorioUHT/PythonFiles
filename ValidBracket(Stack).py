context = str(input())

def isValidBracket(context: str):
    openType,closeType = ["(","{","["],[")","}","]"]
    stack = []
    
    for i in context:
        if i in openType:
            stack.append(i)
        elif i in closeType:
            if not stack: return False
            
            top = stack.pop()
            if (top == "(" and i != ")") or (top == "[" and i != "]") or (top == "{" and i != "}"):
                return False
            
    return len(stack) == 0


print("Valid") if (isValidBracket(context)) else print("Invalid")