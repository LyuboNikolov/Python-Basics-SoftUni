n = int(input())

for row in range(1, n + 1):
    print(" " * (n - row), end="")
    print("*", end="")
    print(" *" * (row - 1))

for row in range(1, n):
    print(" " * row, end="")
    print("*", end="")
    print(" *" * ((n - row) - 1))
