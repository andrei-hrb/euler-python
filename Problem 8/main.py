import os

if __name__ == "__main__":
    file = open(os.getcwd() + "/1000-digit.txt", "r")

    digits = []
    for line in file.readlines():
        for character in line:
            if character.isdigit():
                digits.append(int(character))

    file.close()

    biggest = 0

    for i in range(0, len(digits) - 13):
        product = 1

        for j in range(i, i + 13):
            product *= digits[j]

        if product > biggest:
            biggest = product

    print(biggest)
    # 23514624000
