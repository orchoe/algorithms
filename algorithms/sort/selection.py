"""
    选择排序（升序）
思路：
选择排序是将待排序数组分成两部分，左侧为已排序区域，右侧为未排序区域
每次遍历，找出未排序区域中最小的数，放置于下一个待排序位置（即已排序区域的末尾的下一个位置）
重复 n（n 为数组长度）次后则所有数字都已正确排序
"""


def sort(arr):
    print('Selection Sort')
    n = len(arr)
    for i in range(n):
        # 找到数组中最小的数字，m 为最小数字坐标
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j

        # 将最小值放至下一个待排序位置 i，将原 i 位数字放置于 m 位
        if m != i:
            arr[i], arr[m] = arr[m], arr[i]
