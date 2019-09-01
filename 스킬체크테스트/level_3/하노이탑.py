def solution(n):
    def my_hanoi(num, first, semi, final):
        if num == 1:

            hanoi.append([first, final])

        else:

            my_hanoi(num - 1, first, final, semi)

            my_hanoi(1, first, semi, final)

            my_hanoi(num - 1, semi, first, final)

    hanoi = []

    my_hanoi(n, 1, 2, 3)
    answer = hanoi
    return answer


print(

    solution(3)
)
