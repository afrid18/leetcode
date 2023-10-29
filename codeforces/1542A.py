for i in range(int(input())):
    n = int(input())

    lst = list()
    lst = list(map(int, input().split()))

    evens = odds = 0
    for i in lst:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("Yes" if evens == odds else "No")
