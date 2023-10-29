for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sm = sum(lst)

    if sm < n:
        print(1)
    else:
        print(sm - len(lst))
