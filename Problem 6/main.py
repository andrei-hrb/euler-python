if __name__ == "__main__":
    n = 100

    sum_of_n = (n * (n + 1)) // 2
    sum_of_n_squared = (n * (n + 1) * (2 * n + 1)) // 6

    # 25164150
    print(sum_of_n * sum_of_n - sum_of_n_squared)
