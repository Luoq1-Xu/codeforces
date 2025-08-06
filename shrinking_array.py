def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))

        solve(n, arr)



def solve(n, arr):
    if n < 2:
        print(-1)
        return

    for i in range(1, n):
        if abs(arr[i] - arr[i-1]) <= 1:
            print(0)
            return
        
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        print(-1)
        return

    print(1)

    



main()