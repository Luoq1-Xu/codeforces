def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        a = [int(i) for i in input().strip().split()]

        # n >= 2
        if a[0] > a[1]:
            # If 1st >= 2nd, swap as early as possible (guaranteed to be best possible move)
            a[0], a[1] = a[0] + a[1], 0
            if n == 2:
                print(sum(a)) # If only 2 elements and 1st >= 2nd, no way to get less than 1st + 2nd
                continue
        else:
            # If 1st < 2nd, try to swap 2nd and third if possible (guaranteed to be best possible move)
            if n == 2:
                print(2 * a[0]) # Don't swap to be optimal
                continue
            # Otherwise, swap 2nd and 3rd
            a[1], a[2] = a[1] + a[2], 0

        # Calculate and print sum of prefix mins
        smallest = a[0]
        ans = smallest
        for i in range(1, n):
            smallest = min(smallest, a[i])
            ans += smallest

        print(ans)

main()