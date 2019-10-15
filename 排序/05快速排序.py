#coding:utf-8
def quick_sort(arr,first,end):
    '''
    快速排序.不新建列表，加起始位置
    :param arr: 待排序的列表
    :param first: 待排序的列表的起始位置
    :param end: 待排序的列表结束位置
    :return:无
    选择待排序数组的第一个元素pivot，确定它的位置.
    '''
    l = arr[first:end+1]
    if first >= end:
        return
    pivot = arr[first]
    left = first# 数组头部指针
    right = end# 数组尾部指针

    while left< right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivot
    quick_sort(arr,first,left-1)
    quick_sort(arr,left+1,end)

arr = [54,26,93,17,77,31,44,55,20]
print(arr)
n = len(arr)-1
quick_sort(arr,0,n)
print(arr)