def multiple_of_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0


if __name__ == "__main__":
    _sum = 0

    for number in range(1, 1000):
        if multiple_of_3_or_5(number):
            _sum = _sum + number

    print(_sum)
    # 233168
