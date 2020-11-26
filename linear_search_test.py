def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 9, 8, 7]
x = 9
result = linear_search(L, x)
print(result)