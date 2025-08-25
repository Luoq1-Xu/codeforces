def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        solve(n, a, b)

def solve(n, a, b):
    net_diff = 0

    for i in range(n):
        if a[i] > b[i]:
            net_diff += (a[i] - b[i])

    print(net_diff + 1) # Plus 1 because the iteration with no change is counted

        

main()