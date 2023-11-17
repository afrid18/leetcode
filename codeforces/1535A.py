for _ in range(int(input())):
    lst = list(map(int, input().split()))
    srtList = sorted(lst)
    hs = set()
    hs.add(srtList[-1])
    hs.add(srtList[-2])

    print("Yes" if max(lst[0], lst[1]) in hs and max(lst[2], lst[3]) in hs else "No")


