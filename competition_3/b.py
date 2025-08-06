def main():
    import sys
    import math
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        a, b, k = (int(i) for i in input().strip().split())

        used = set()

        # Want to reuse the same move as much as possible
        # Find the best move and keep reusing it

        # auto win condition 1
        if a <= k and b <= k:
            print(1)
            continue

        # auto win condition 2
        g = math.gcd(a, b)
        x_step = a // g
        y_step = b // g

        if x_step <= k and y_step <= k:
            print(1)
            continue

        # Else, can accomplish in cost 2 (0, 1) and (1, 0) all the way
        print(2)

main()