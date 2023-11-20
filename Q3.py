n = 8
for i in range(1, n + 1):
    for j in range(n, i, -1):
        print("   ",end="")

    for j in range(1, i+1):
        x = 2**(j-1)
        print(x, end=" ")

    for j in range(i - 1, 0, -1):
         x = 2**(j - 1)
         print(x, end=" ")

    print()
