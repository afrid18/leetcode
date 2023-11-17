for _ in range(int(input())):
    n = int(input())
    s = input()
    hs = set()

    ln = len(s)
    i = 0
    res = "YES"
    while(i < ln - 1):
        if(s[i] != s[i + 1]):
            if(s[i] in hs):
                res = "NO"
                break
            hs.add(s[i])
        # if(s[i] in hs):
           #  res = "NO"
            # break
        i += 1
    if(s[ln - 1] in hs):
        res = "NO"
    print(res)
