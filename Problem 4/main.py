def is_palindrome(n):
    copy = n
    _reverse = 0

    while copy:
        _reverse = _reverse * 10 + copy % 10
        copy //= 10

    return _reverse == n


if __name__ == "__main__":
    biggest = 0

    for first in range(100, 999):
        for second in range(100, 999):
            _num = first * second
            if is_palindrome(_num) and _num > biggest:
                biggest = _num

    print(biggest)
    # 906609
