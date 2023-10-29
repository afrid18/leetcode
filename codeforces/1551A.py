n = int(input())

for i in range(n):
    inp = int(input())

    equals = inp // 3
    if equals * 3 == inp:
        print(equals, equals)
    elif equals * 3 + 1 == inp:
        print(equals + 1, equals)
    else:
        print(equals, equals + 1)

