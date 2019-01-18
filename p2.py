p1 = int(input("<+>"))


def f(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, int(value / i)))
    return factors


p2 = f(p1)


def ps(n):
    # Trivial checks
    if isinstance(n, int) is not True:  # integer
        return False
    if n < 0:      # positivity
        return False
    if n == 0:      # 0 pass
        return True

    # Reduction by powers of 4 with bit-logic
    while n & 3 == 0:
        n = n >> 2

    # Simple bit-logic test. All perfect squares, in binary,
    # end in 001, when powers of 4 are factored out.
    if n & 7 != 1:
        return False

    if n == 1:
        return True  # is power of 4, or even power of 2

    # Simple modulo equivalency test
    c = n % 10
    if c in {3, 7}:
        return False  # Not 1,4,5,6,9 in mod 10
    if n % 7 in {3, 5, 6}:
        return False  # Not 1,2,4 mod 7
    if n % 9 in {2, 3, 5, 6, 8}:
        return False
    if n % 13 in {2, 5, 6, 7, 8, 11}:
        return False

    # Other patterns
    if c == 5:  # if it ends in a 5
        if (n//10) % 10 != 2:
            return False    # then it must end in 25
        if (n//100) % 10 not in {0, 2, 6}:
            return False    # and in 025, 225, or 625
        if (n//100) % 10 == 6:
            if (n//1000) % 10 not in {0, 5}:
                return False    # that is, 0625 or 5625
    else:
        if (n//10) % 4 != 0:
            return False    # (4k)*10 + (1,9)

    # Babylonian Algorithm. Finding the integer square root.
    # Root extraction.
    s = (len(str(n))-1) // 2
    x = (10**s) * 4

    A = {x, n}
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in A:
            return False
        A.add(x)
    return True


print(p2)
for pair in p2:
    print(f"{pair} ({ps(pair[0])}, {ps(pair[1])})")

input("press enter to close")
