from itertools import product


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    max_subscribe_count, max_price = 0, 0

    for discount_combination in product(discount_rates, repeat=len(emoticons)):
        subscribe_count = 0
        total_price = 0

        for user_discount, user_threshold in users:
            user_total = 0
            for rate, price in zip(discount_combination, emoticons):
                if rate >= user_discount:
                    user_total += price * (100 - rate) / 100
            if user_total >= user_threshold:
                subscribe_count += 1
            else:
                total_price += user_total

        if (subscribe_count > max_subscribe_count) or (
                subscribe_count == max_subscribe_count and total_price > max_price):
            max_subscribe_count, max_price = subscribe_count, total_price

    return [max_subscribe_count, int(max_price)]
