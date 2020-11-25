def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i

    return -1


L = [3, 1, 0, 7, 9, 5]
x = 8
a = linear_search(L, x)
print(a)