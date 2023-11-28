def solve():
    n = int(input())
    lst = list(map(int, input().split()))

    ans = 0

    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            ans += abs(lst[i] - lst[i - 1])
            lst[i] = lst[i - 1]

    print(ans)


if __name__ == '__main__':
    solve()
