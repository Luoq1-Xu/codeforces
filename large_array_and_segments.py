def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, k, x = (int(i) for i in input().strip().split())
        arr = list(map(int, input().strip().split()))
        solve(n, k, x, arr)



def solve(n, k, x, arr):
    arr_sum = sum(arr)
    multiples = x // arr_sum
    remainder = x - (multiples * arr_sum)

    if multiples > k or (multiples == k and remainder > 0):
        print(0)
        return

    if remainder == 0:
        print((n * k) - (multiples * n) + 1)
        return

    # Go backwards, find the first index that can cover the remainder
    cum_sum = 0
    index = -1
    for i in range(n - 1, -1, -1):
        cum_sum += arr[i]
        if cum_sum >= remainder:
            index = i
            break

    print((n * k) - (multiples * n) - (n - index - 1))

main()