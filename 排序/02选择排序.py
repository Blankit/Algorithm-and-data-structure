# coding:utf-8
def select_sort(arr):
    '''
    选择排序
    每次遍历数组，选出最小（或最大）的元素，与列表前面部分的元素交换位置
    :param arr:
    :return:
    '''
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
arr = [54,26,93,17,77,31,44,55,20]
print(arr)
select_sort(arr)
print(arr)
