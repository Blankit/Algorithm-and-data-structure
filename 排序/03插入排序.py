#coding:utf-8
def insert_sort(arr):
    '''
    插入排序
    保证列表前面是有序的。
    从列表后面部分，有一次选择元素，插入列表前面部分
    :param arr:
    :return:
    '''
    n = len(arr)
    for i in range(1,n):
        while i > 0:
            if arr[i] > arr[i-1]:
                i -= 1
            else:
                arr[i],arr[i-1] = arr[i-1],arr[i]
arr = [54,26,93,17,77,31,44,55,20]
print(arr)
insert_sort(arr)
print(arr)
