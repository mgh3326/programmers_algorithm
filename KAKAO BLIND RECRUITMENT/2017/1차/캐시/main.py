def solution(cacheSize, cities):
    answer = 0
    cache_list = []
    for city in cities:
        city = city.lower()
        if city in cache_list:  # hit
            answer += 1
            cache_list.pop(cache_list.index(city))
            cache_list.append(city)  # LRU 적용 위해 사용된걸 맨 뒤로 보낸다

        else:
            answer += 5  # miss
            if cacheSize == 0:
                continue
            if len(cache_list) == cacheSize:
                cache_list.pop(0)
            cache_list.append(city)

    return answer


cacheSize_list = [
    3, 3, 2, 5, 2, 0
]
cities_list = [
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
    ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    ["Jeju", "Pangyo", "NewYork", "newyork"],
    ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
]

return_list = [
    50, 21, 60, 52, 16, 25
]
for _input_data in zip(cacheSize_list, cities_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(cacheSize_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
