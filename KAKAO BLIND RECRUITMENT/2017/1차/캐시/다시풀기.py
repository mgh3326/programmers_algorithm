def solution(cacheSize, cities):
    answer = 0
    cache_list = [""] * cacheSize
    for city in cities:
        city = city.lower()
        if city in cache_list:
            pop = cache_list.pop(cache_list.index(city))
            cache_list.append(pop)
            answer += 1

        else:
            cache_list.append(city)
            cache_list.pop(0)

            answer += 5
    return answer


print(
    solution(
        3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    )
)
