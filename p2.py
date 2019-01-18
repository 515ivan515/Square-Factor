p1 = int(input("<+>"))


def f(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append([i, int(value / i)])
    return factors


p2 = f(p1)


def ps(n):
    if isinstance(n, int) is not True:
        return False
    if n < 0:
        return False
    if n == 0:
        return True
    while n & 3 == 0:
        n = n >> 2
    if n & 7 != 1:
        return False
    if n == 1:
        return True
    c = n % 10
    if c in {3, 7}:
        return False
    if n % 7 in {3, 5, 6}:
        return False
    if n % 9 in {2, 3, 5, 6, 8}:
        return False
    if n % 13 in {2, 5, 6, 7, 8, 11}:
        return False
    if c == 5:
        if (n//10) % 10 != 2:
            return False
        if (n//100) % 10 not in {0, 2, 6}:
            return False
        if (n//100) % 10 == 6:
            if (n//1000) % 10 not in {0, 5}:
                return False
    else:
        if (n//10) % 4 != 0:
            return False
    s = (len(str(n))-1) // 2
    x = (10**s) * 4
    A = {x, n}
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in A:
            return False
        A.add(x)
    return True

notp2 = []
arep2 = []
print(p2)
for pair in p2:
    if ps(pair[0]) is False and ps(pair[1]) is False:
        notp2.append([pair, [ps(pair[0]), ps(pair[1])]])
    elif ps(pair[0]) is True or ps(pair[1]) is True:
        arep2.append({
            ps(pair[0]): pair[0],
            ps(pair[1]): pair[1]
        })
    print(f"{pair} ({ps(pair[0])}, {ps(pair[1])})")
smallp2 = {True: 1, False: 9999}
for pair in arep2:
    if pair[False] < smallp2[False]:
        smallp2 = {True: pair[True], False: pair[False]}
print(smallp2)
print(notp2)
print(arep2)
input("press enter to close")
