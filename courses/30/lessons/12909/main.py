def solution(s):
    stack = []
    for value in s:
        if value == "(":
            stack.append(value)
        else:  # value == ")"
            if not stack:
                return False
            stack.pop()
    return not stack
