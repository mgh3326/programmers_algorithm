def solution(word, pages: list):
    base_score_list = []
    origin_url_dict = {}
    word = word.lower()
    link_list = []
    for page_idx, page in enumerate(pages):
        origin_url = page.split("<meta property=\"og:url\" content=\"")[1].split("\"/>")[0]
        origin_url_dict[origin_url] = page_idx
        # page = page.split("<body>")[1].split("</body")[0]
        # page_tag_split_list = page.split("<")
        # page_text = page_tag_split_list[0]
        # for page_tag_split in page_tag_split_list[1:]:
        #     page_text += page_tag_split.split(">")[1]

        page_lower = page.lower()

        split_list = page_lower.split(word)
        count = 0
        if len(split_list) == 1:
            pass
        else:
            for split_idx, split in enumerate(split_list[:-1]):
                if len(split_list[split_idx + 1]) == 0 or len(split) == 0:
                    continue
                if split[-1].isalpha() or split_list[split_idx + 1][0].isalpha():
                    pass
                else:
                    count += 1
        base_score_list.append(count)
    total_score_list = base_score_list.copy()

    for page_idx, page in enumerate(pages):

        hyper_link_list = page.split("<a href=\"")[1:]
        for hyper_link in hyper_link_list:
            split_ = hyper_link.split("\"")[0]
            if split_ in origin_url_dict:
                total_score_list[origin_url_dict[split_]] += (base_score_list[page_idx] / len(hyper_link_list))

    answer = total_score_list.index(max(total_score_list))
    return answer


word_list = [
    "blindddddd",
    "Muzi",
    "Muzi",
    "aba",
    "hi",
]
pages_list = [
    [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"],
    [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"],
    [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzimuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"],
    [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!abab abababa!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tabaabaaba<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"],

    [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nhi hello \n<a href=\"https://d.com\"> Link to d </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nhi pi lo Hi hi HI vi\n<a href=\"https://a.com\"> Link to a </a>\n<a href=\"https://d.com\"> Link to d </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nhi hi hi HI HI hi hi hi hi good\n<a href=\"https://a.com\"> Link to a </a>\n<a href=\"https://d.com\"> Link to d </a>\n<a href=\"https://e.com\"> Link to e </a>\n</body>\n</html>"],
]

return_list = [
    0, 1, 1, 2, 0
]
for _input_data in zip(word_list, pages_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(word_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
