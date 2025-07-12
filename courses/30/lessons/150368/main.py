import collections


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    discount_rates.reverse()
    # 10%, 20%, 30%, 40%
    # 이모티콘의 할인에 따른 조합을 만들어서, 이모티콘 플러스 구독이 많게 할 할인율을 뽑기가 최우선, 그 이후
    emoticon_discount_rates_list = []

    deque = collections.deque([])
    deque.append(([], 0))
    while deque:
        _list, depth = deque.pop()
        if depth == len(emoticons):
            emoticon_discount_rates_list.append(_list)
            continue
        for rate in discount_rates:
            deque.append((_list + [rate], depth + 1))

    max_subscribe_count = 0
    max_price = 0
    for emoticon_discount_rates in emoticon_discount_rates_list:
        subscribe_count = 0
        price_sum = 0
        for user in users:
            user_price_sum = 0
            user_max_discount_rate, price_threshold = user
            for emoticon_discount_rate_idx in range(len(emoticon_discount_rates)):
                emoticon_discount_rate = emoticon_discount_rates[emoticon_discount_rate_idx]
                if user_max_discount_rate > emoticon_discount_rate:
                    continue
                emoticon = emoticons[emoticon_discount_rate_idx]
                _price = emoticon - ((emoticon_discount_rate / 100) * emoticon)
                user_price_sum += _price
            if user_price_sum >= price_threshold:
                subscribe_count += 1
                user_price_sum = 0
            price_sum += user_price_sum
        if max_subscribe_count < subscribe_count:
            max_subscribe_count = subscribe_count
            max_price = price_sum
        elif max_subscribe_count == subscribe_count:
            if max_price < price_sum:
                max_price = price_sum
    return [max_subscribe_count, int(max_price)]
