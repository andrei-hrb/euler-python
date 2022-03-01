import math


if __name__ == "__main__":
    biggest_divisor = 0
    special_number = 600851475143

    # redundant in this case, but just for the sake of it
    while special_number % 2 == 0:
        special_number /= 2
        biggest_divisor = 2

    for divisor in range(3, int(math.sqrt(special_number)), 2):
        while special_number % divisor == 0:
            special_number /= divisor
            biggest_divisor = divisor

    print(biggest_divisor)
    # 6857
