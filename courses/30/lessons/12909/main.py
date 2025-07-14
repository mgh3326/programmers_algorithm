def solution(s):
    answer = True
    stack = []
    for value in s:
        if value == "(":
            stack.append(value)
        elif value == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    return answer
