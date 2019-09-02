import heapq


def solution(genres, plays):
    my_dict = {}
    sum_dict = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in my_dict:
            my_dict[genre] = []
            sum_dict[genre] = 0
        heapq.heappush(my_dict[genre], (-1 * play, i))
        sum_dict[genre] += play
    sum_dict = sorted(sum_dict.items(), key=lambda t: t[1], reverse=True)
    answer = []
    for sum_dict_key, value in sum_dict:
        for i in range(2):
            if len(my_dict[sum_dict_key]) != 0:
                heappop = heapq.heappop(my_dict[sum_dict_key])
                answer.append(heappop[1])
    return answer


print(

    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
# [4, 1, 3, 0]
