# brute force lol

from cmath import sqrt


def is_prime(number):
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    div = 5
    while div * div <= number:
        if number % div == 0:
            return False
        div += 2

    return True


if __name__ == "__main__":
    cnt = 1
    for number in range(3, 8000000000, 2):
        if is_prime(number):
            cnt += 1
            if cnt == 10001:
                print(number)
                break
