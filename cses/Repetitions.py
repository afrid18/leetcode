def solve():
    s = input()
    count = 1

    mx_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            mx_len = max(mx_len, count)
            count = 1
    print(max(mx_len, count))


if __name__ == '__main__':
    solve()
