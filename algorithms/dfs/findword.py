def exists(word, raw_arr):
    """
    查找二维数组中是否存在目标单词，即数组中连续的字母能够组成目标单词
    :param word: 待查单词
    :param raw_arr: 字母二维数组
    :return: boolean
    """

    # 遍历整个数组，记录 word 中每个字母在数组中的位置
    letter_dic = dict()
    for x in range(len(raw_arr)):
        for y in range(len(raw_arr[x])):
            letter = raw_arr[x][y]
            if letter in letter_dic:
                letter_dic[letter].append([x, y])
            else:
                letter_dic[letter] = [[x, y]]

    # 初始化一个与 word 等长的数组，用来记录 word 中每个字母的可选位置
    pos_record = []
    for n in range(len(word)):
        pos_record.append(letter_dic[word[n]])

    print(pos_record)

    # 位置筛选规则：相邻的两个点距离为1，相间的两个点距离为2
    for i in range(len(pos_record) - 1):
        if not is_adjacent(pos_record[i], pos_record[i + 1]):
            return False
        if i > 0 and not is_separate(pos_record[i - 1], pos_record[i + 1]):
            return False

    return True


# 判断连点是否相邻
def is_separate(pre, nxt):
    for p in pre:
        for n in nxt:
            if (abs(p[0] - n[0]) == 1 and abs(p[1] - n[1]) == 1) \
                    or (p[0] == n[0] and abs(p[1] - n[1]) == 2) \
                    or (abs(p[0] - n[0]) == 2 and p[1] == n[1]):
                return True
    return False


# 判断两点是否相间
def is_adjacent(cur, nxt):
    for c in cur:
        for n in nxt:
            if (abs(c[0] - n[0]) == 1 and c[1] == n[1]) \
                    or (c[0] == n[0] and abs(c[1] - n[1]) == 1):
                return True
    return False


def main():
    word = "drot"
    arr = [
        ['a', 'c', 'd', 'z'],
        ['t', 'x', 'r', 'n'],
        ['o', 'i', 'o', 'm']
    ]

    print([1] * 6)

    print(exists(word, arr))


if __name__ == '__main__':
    main()
