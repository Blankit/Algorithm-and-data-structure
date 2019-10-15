#coding:utf-8
def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            while i > 0:
                if arr[i]>arr[i-gap]:
                    i -= gap
                else:
                    arr[i],arr[i-gap]=arr[i-gap],arr[i]
        gap = gap // 2
arr = [54,26,93,17,77,31,44,55,20]
# arr = [54,26,93,17]
print(arr)
shell_sort(arr)
print(arr)

