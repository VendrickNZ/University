import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    def fibonacci(n):
        current, sums, count = 0, 1, 0
        for num in range(n):
            print(sums, num)
            if (sums + num) % 2 == 0:
                current, sums = sums, sums + num
                count = sums
            else:
                current, sums = sums, sums + num

        return count

    print(fibonacci(n))