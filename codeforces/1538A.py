def solve():
    n = int(input())
    lst = list(map(int, input().split()))

    mx = max(lst)
    mn = min(lst)

    mx_idx = lst.index(mx)
    mn_idx = lst.index(mn)



    if mx_idx < n / 2 and mn_idx >= n / 2 or mn_idx > n / 2 and mx_idx <= n / 2:
        print(min(mx_idx, len(lst) - mx_idx) + min(mn_idx , len(lst) - mn_idx) + 1)
    else:
        print(min(min(mx_idx, n - mx_idx) + 1, min(mn_idx, n - mn_idx) + 1))



if __name__ == '__main__':
  for _ in range(int(input())):
    solve()
