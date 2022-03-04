if __name__ == "__main__":
    sieve = [False] * 2000001

    p = 2

    while p <= 2000000:
        if sieve[p] == False:
            i = 2
            while i * p <= 2000000:
                sieve[i * p] = True
                i += 1
        p += 1

    sum = 0

    for i in range(2, 2000000):
        if sieve[i] == False:
            sum += i

    print(sum)
    # 142913828922
