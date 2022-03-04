if __name__ == "__main__":
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a * a + b * b == c * c and a + b + c == 1000:
                    print(a * b * c)
                    # 31875000
                    quit()
