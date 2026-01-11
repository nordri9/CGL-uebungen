import random


def split(left, right):
    pivot = data[right]
    i = left - 1  # place for the next <= pivot
    for j in range(left, right):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    # place pivot after the last <= pivot element
    data[i + 1], data[right] = data[right], data[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        spliter = split(left, right)
        quick_sort(left, spliter - 1)
        quick_sort(spliter + 1, right)


n = 200
data = random.sample(range(1, n + 1), n)
print("before:", data)
quick_sort(0, len(data) - 1)
print("after :", data)
