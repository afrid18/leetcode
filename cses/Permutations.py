def solve():
    n = int(input())
    lst = list()
    if n in [2, 3]:
        print("NO SOLUTION")
        return
    elif n == 4:
        print("2 4 1 3")
        return
    else:
        max_even = n if n % 2 == 0 else n - 1
        max_odd = n - 1 if n % 2 == 0 else n
        # print(max_even, max_odd)

        for i in range(max_even, 0, -2):
            # lst.append(i)
            print(i, end=" ")
        for i in range(max_odd, 0, -2):
            # lst.append(i)
            print(i, end=" ")



if __name__ == '__main__':
    solve()
