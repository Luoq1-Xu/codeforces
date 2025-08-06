def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))

        # If it is possible to explode, these two equations must be obeyed.
        # Let X be the number of operation 1s, and Y be the number of operation 2s
        # 1 -> a1 = X + nY
        # 2 -> an (nth element) = nX + y

        # Thus, x = (a1 - n * an) / (1 - n^2) -> This must be an integer.
        # y = an - nX

        # First check if possible
        x = (arr[0] - (n * arr[-1])) / (1 - n**2)
        y = arr[n-1] - (x * n)

        if not x.is_integer() or x < 0 or y < 0:
            # Not possible to find an integer value of x
            print("NO")
            continue

        can_explode = True
        # Now check if all elements obey the pattern
        for i in range(n):
            if arr[i] != (x * (i + 1)) + (y * (n - i)): # 1-indexed
                # not possible
                can_explode = False
                break
        
        if can_explode:
            print("YES")
        else:
            print("NO")


main()