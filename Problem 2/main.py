def is_even(n):
    return not n % 2


if __name__ == "__main__":
    _sum = 0

    first = 1
    second = 2

    while second < 4000000:
        if is_even(second):
            _sum = _sum + second
        aux = first
        first = second
        second = second + aux

    print(_sum)
    # 4613732
