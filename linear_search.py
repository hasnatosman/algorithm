def linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i += 1
    i = -1
    return -1


L = [0, 2, 4, 7, 3, 9]
x = 3
a = linear_search(L, x)
print(a)
