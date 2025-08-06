def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    ans = [0] * n

    largest_at_i = [0] * n
    largest = arr[0]
    for i in range(n):
        largest = max(largest, arr[i])
        largest_at_i[i] = largest

    cum_sum = 0
    for i in range(n-1, -1, -1):
        # If move is better, do it
        if largest_at_i[i] > arr[i]:
            ans[n - i - 1] = cum_sum + largest_at_i[i]
        else:
            ans[n - i - 1] = cum_sum + arr[i]

        cum_sum += arr[i]

    print(" ".join(map(str, ans)))


main()