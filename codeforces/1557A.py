for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    mx = max(lst)
    ln = len(lst)

    ans = ((sum(lst) - mx) / (ln - 1)) + mx
    print(round(ans, 9))
