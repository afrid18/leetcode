def solve():
    n = int(input())

    i = 1
    while(i * i < n):
        i += 1
    print(i)


if __name__ == '__main__':
  for _ in range(int(input())):
    solve()
