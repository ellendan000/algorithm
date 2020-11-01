import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = math.ceil((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 9, 11]
    print(binary_search(my_list, 11))
    print(binary_search(my_list, -1))
