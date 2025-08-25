from collections import deque
def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())

    # Make exactly n using the minimum number of 3^x.

    # Convert to base 3 representation
    rem = []
    while n > 0:
        remainder = n % 3
        rem.append(remainder)
        n = n // 3

    ans = 0
    for i in range(len(rem)):
        ans += rem[i] * ((3**(i+1)) + (i * (3**(i-1))))

    print(int(ans))
    return

main()