import itertools


def solution(expression):
    answer = 0
    operators = ['-', '*', '+']
    numbers = []
    ops = []
    temp = ''

    for char in expression:
        if char in operators:
            numbers.append(int(temp))
            ops.append(char)
            temp = ''
        else:
            temp += char

    if temp:  # 맨 마지막에 남은 문자열 처리
        numbers.append(int(temp))

    def calculate(op, num1, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        else:
            raise Exception("Invalid operator")

    operator_permutations = list(itertools.permutations(list(set(ops))))
    for operator_permutation in operator_permutations:
        current_numbers = numbers[:]
        current_ops = ops[:]
        for operator in operator_permutation:
            while operator in current_ops:
                operator_index = current_ops.index(operator)
                result = calculate(operator, current_numbers[operator_index], current_numbers[operator_index + 1])
                current_numbers[operator_index] = result
                current_numbers.pop(operator_index + 1)
                current_ops.pop(operator_index)
        answer = max(answer, abs(current_numbers[0]))
    return answer
