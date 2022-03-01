def gcd(a, b):
    if a == 0 or b == 0:
        return a or b

    return gcd(b, (a % b))


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    value = 1

    for number in range(2, 20):
        value = lcm(value, number)

    print(value)
    # 232792560
