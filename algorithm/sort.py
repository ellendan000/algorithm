import math

def selection_sort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middleIndex = math.ceil((len(array)-1)/2)
        left = merge_sort(array[:middleIndex])
        right = merge_sort(array[middleIndex:])
        if left < right:
            return left + right
        else:
            return right + left

