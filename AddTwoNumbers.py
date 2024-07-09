# SEE:  https://leetcode.com/problems/add-two-numbers/

def addTwoNumbers( l1: list , l2: list ) -> list:
    rl1 = l1[::-1]
    rl2 = l2[::-1]
    sl1 = "".join(map(str, rl1))
    sl2 = "".join(map(str, rl2))
    sum = int(sl1) + int(sl2)
    final = list(map(int, str(sum)))
    return final[::-1]


def test_addTwoNumbers():
    assert  addTwoNumbers([2 ,4 ,3] ,[5 ,6 ,4]) == [7 ,0 ,8]
    assert  addTwoNumbers([3 ,4 ,2] ,[4 ,6 ,5]) == [7 ,0 ,8]    # 243 + 564 = 807 -> [7,0,8]

    