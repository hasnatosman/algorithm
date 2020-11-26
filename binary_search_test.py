def binary_search(list, a):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left+right) // 2
        if list[mid] == a:
            return mid
        if list[mid] < left:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    list = [1, 2, 3, 4]
    a = 1
    item = binary_search(list, a)
    print(item)