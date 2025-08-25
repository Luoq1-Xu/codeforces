def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        solve(n)

def solve(n):
    # Find lexographically smallest array such that:
    # 1. product of adjacent elements is negative
    # 2. all subarrays of len 2 or longer is positive

    # must use -1s -> smallest possible
    ans = []

    for i in range(n - 1):
        if i % 2 == 0:
            ans.append("-1")
        else:
            ans.append("3")

    if n % 2 == 0:
        ans.append("2")
    else:
        ans.append("-1")

    print(" ".join(ans))

main()