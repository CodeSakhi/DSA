# number of rows (half diamond height)
n = 5

# upper triangle
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# lower triangle
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
