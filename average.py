def aver(L):
    if not L:
        return None
    else:
        return sum(L)//len(L)


if __name__ == "__main__":
    L = [11, 22, 33, 44, 55, 66, 77, 88]
    average = aver(L)
    print("Average is: ", average)