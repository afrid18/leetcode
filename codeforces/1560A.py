for _ in range(int(input())):
    n = int(input())
    ctr = 1
    curr = 1
    while(True):
        if ctr == n:
            print(curr)
            break
        else:
            curr += 1
            if curr % 3 == 0 or curr % 10 == 3:
                continue
            else:
                ctr += 1

            
