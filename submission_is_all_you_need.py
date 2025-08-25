def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # Max scores -> sum of all positive + number of zeroes
    zeroes = 0
    for num in arr:
        if num == 0:
            zeroes += 1

    print(sum(arr) + zeroes)

main()