def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n, c = (int(i) for i in input().strip().split())
    arr = list(map(int, input().strip().split()))

    ans = 0
    arr.sort(reverse=True)
    for e in arr:
        if e << ans <= c:
            ans += 1

    print(n - ans)


main()