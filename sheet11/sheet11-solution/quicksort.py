import random


def split(left, right):
    i = left
    j = right - 1
    pivot = data[right]
    while i < j:
        while i < j and data[i] <= pivot:
            i += 1
        while j > i and data[j] > pivot:
            j -= 1
        if i < j and data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
            # i += 1
            # j -= 1
    if data[i] > pivot:
        data[i], data[right] = data[right], data[i]
    else:
        i = right
    return i


def quick_sort(left, right):
    if left < right:
        spliter = split(left, right)
        quick_sort(left, spliter - 1)
        quick_sort(spliter + 1, right)


n = 400
data = random.sample(range(1, n+1), n)
print("before:", data)
left = 0
right = len(data) - 1
quick_sort(left, right)
print("after :", data)
