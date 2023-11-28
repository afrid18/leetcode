def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    real_sum = n * (n + 1) // 2

    print(real_sum - sum(lst))


if __name__ == '__main__':
    solve()
