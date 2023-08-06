#!/usr/bin/python3

import sys


def factorize(n):
    """Factorize as many numbers as possible into a product
    of two smaller numbers
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return None, None


def main(file_name):
    """Factorize as many numbers as possible into a product
    of two smaller numbers
    """
    with open(file_name, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        num = int(num)
        p, q = factorize(num)
        if p is not None:
            print(f"{num}={p}*{q}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    main(file_name)
