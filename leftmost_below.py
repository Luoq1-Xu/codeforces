def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip()) 
    arr = list(map(int, input().strip().split()))

    curr_min = arr[0]

    for i in range(1, n):
        if arr[i] >= 2 * curr_min:
            print("NO")
            return
        curr_min = min(curr_min, arr[i])
        
    print("YES")

main()