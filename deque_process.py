from typing import List, Tuple

def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, x = (int(i) for i in input().strip().split())
        solve(n, x)

def solve(n, x):
    ans = []

    if x % 2 == 0:
        # MEX is always 1, since impossible to include 1
        for _ in range(n - 1):
            ans.append("0")
        ans.append(str(x))
        print(" ".join(ans))
        return
    
    # Otherwise, try to add 1, 2, 3... until impossible
    
    # Get binary representation of x
    binary_x = bin(x)[2:]

    # Find first zero from backwards -> this tells us max we can count up to
    # If we encounter 0 at any point, we know that we need to supplement (since python has no leading zeroes in bin representation)
    max_num = 1
    multiple = 1
    zero_found = False
    for i in range(len(binary_x) - 2, -1, -1):
        if int(binary_x[i]) == 0:
            zero_found = True
            break
        multiple *= 2
        max_num += multiple

    # If no zero found, x can be made entirely of ORS of [0, max_num]
    if not zero_found:
        if multiple + 1 <= n:
            ans = [str(i) for i in range(min(n, max_num + 1))]
        else:
            ans = [str(i) for i in range(n - 1)]
    else:
        # Zero found, must add one x at the end regardless
        ans = [str(i) for i in range(min(n - 1, max_num + 1))]

    while len(ans) < n:
        ans.append(str(x))

    print(" ".join(ans))

main()