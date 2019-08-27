def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
# or 연산을 이용했으며,
# 파이썬 이진수 변환과, rjust를 활용하면 짧은 코드로 풀린다.
