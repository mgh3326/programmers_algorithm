def solution(phone_book):
    phone_book_count_list_dict = {}
    for p in phone_book:
        if len(p) in phone_book_count_list_dict:
            phone_book_count_list_dict[len(p)].append(p)
        else:
            phone_book_count_list_dict[len(p)] = [p]
    for phone_book_count in phone_book_count_list_dict:
        for _phone_book_list in phone_book_count_list_dict[phone_book_count]:
            for temp in list(phone_book_count_list_dict.values())[
                        list(phone_book_count_list_dict.keys()).index(phone_book_count) + 1:]:
                for _temp in temp:
                    if _phone_book_list == _temp[:len(_phone_book_list)]:
                        answer = False
                        return answer

    answer = True
    return answer


phone_book_list = [
    ["119", "97674223", "1195524421"],
    ["123", "456", "789"],
    ["12", "123", "1235", "567", "88"]
]
return_list = [
    False,
    True,
    False
]

for _p, _r in zip(phone_book_list, return_list):
    print("index : ", phone_book_list.index(_p))
    result = solution(_p)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
