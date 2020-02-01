""" 冒泡排序 """


def sort(arr):
    print('Bubble Sort')
    n = len(arr)
    flag = False
    for i in range(n):
        # 每一轮冒泡，都可以将本轮最大数的放置到正确的位置
        for j in range(0, n - i - 1):
            # 若 arr[j] 大于 arr[j+1], 将大数向后放置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 说明本轮有数据交换
                flag = True

        # 若本轮没有发生交换，说明已经排序完成
        if not flag:
            break
