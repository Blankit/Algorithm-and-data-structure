# coding:utf-8
'''
冒泡排序，每次与后面一个元素比较
不符合大小关系，则交换元素位置
'''
def bubble(arr):
    l = len(arr)
    k = 1
    for i in range(l-1):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(k,' ',arr)
        k += 1
arr = [54,26,93,17,77,31,44,55,20]
print(arr)
bubble(arr)
# print(arr)
