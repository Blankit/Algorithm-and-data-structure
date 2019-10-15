#coding:utf-8
def merge_sort(arr):
    '''
    归并排序
    先将数组对分对分，直至变成单个元素
    然后两两比较合并，知道变成一个有序的序列
    归并排序过程比较像中根遍历的过程
    :param arr:
    :return:
    '''
    if len(arr) <=1 :
        return arr
    n = len(arr)
    mid = n //2
    left = merge_sort(arr[:mid])# 返回一个列表
    right = merge_sort(arr[mid:])
    result= []
    left_index = 0# 指向左边的数组
    right_index = 0# 指向右边的数组
    while left_index<len(left) and right_index < len(right):
        # 任一列表遍历到尾部，跳出循环
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:] #剩余部分
    result += right[right_index:]
    return result
arr = [54,26,93,17,77,31,44,55,20]
# arr = [54,26,93,17]
print(arr)
result = merge_sort(arr)
print(result)