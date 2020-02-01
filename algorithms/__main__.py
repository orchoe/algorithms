import os
import sys

root_path = os.path.abspath(os.path.dirname('.'))
sys.path.append(root_path)
from algorithms.methods import bubble, bucket, insertion, merge, quick, selection


def main(args):
    # 示例待排序数组，升序排列
    arr = [2, 6, 8, 7, 1, 4, 5]
    print(f'Before: {arr}')
    eval(args[1] + '.sort')(arr)
    # 打印排序后的数组
    print(f'After: {arr}')


if __name__ == '__main__':
    main(sys.argv)
