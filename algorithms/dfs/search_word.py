def exists(word, board):
    """
    查找二维数组中是否存在目标单词，即数组中连续的字母能够组成目标单词
    :param word: 待查单词
    :param board: 字母二维数组
    :return: bool
    """

    # 记录数组的长和宽
    xbound = len(board)
    ybound = len(board[0])

    # 创建一个二维数组记录可行的轨迹
    mem = [[0] * ybound for _ in range(xbound)]

    # 定义一个tuple，表示每个位置四种不同的方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 查找方法，每一个点递归查找四个方向
    # 满足条件的话会一直递归，直到查找完所有字母
    def search(x, y, idx):
        # 若单词中的最后一位字母已经查找过，说明查找完成
        if idx == len(word):
            return True

        # 若出边界或者该点已经走过，或该点不是当前查找的字母，说明查找失败
        if x < 0 or x >= xbound or y < 0 or y >= ybound or mem[x][y] or board[x][y] != word[idx]:
            return False

        # 说明该点字母与要查找的字母相符，将该点标记为查找过
        mem[x][y] = 1

        # 从该点开始，向四个可能的方向分别查找单词中的下一个字母
        for (i, j) in directions:
            if search(x + i, y + j, idx + 1):
                return True

        # 若四个方向均不可行，将当前的标记置为0，返回查找失败
        mem[x][y] = 0
        return False

    # 从原数组的任意一点出发，判读从该点开始是否有可行的字母轨迹串成目标单词
    for x in range(xbound):
        for y in range(ybound):
            if search(x, y, 0):
                return True

    return False


def main():
    word = "zdroi"
    arr = [
        ['a', 'c', 'd', 'z'],
        ['t', 'x', 'r', 'n'],
        ['o', 'i', 'o', 'm']
    ]

    print(exists(word, arr))


if __name__ == '__main__':
    main()
