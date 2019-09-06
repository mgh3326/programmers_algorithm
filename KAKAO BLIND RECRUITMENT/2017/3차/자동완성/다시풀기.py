class Node:

    """ A node that consists of a trie. """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string


def solution(words):
    answer = 0
    temp_dict = {
        "name": "",
        "child": {},
        "value": 0
    }
    my_dict = {}
    trie = Trie()
    for word in words:
        trie.insert(word)

        print()

    return answer


print(
    solution(
        ["go", "gone", "guild"]
    )
)
