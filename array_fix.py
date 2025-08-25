def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    stk = [arr[-1]]
    for i in range(n-2, -1, -1):
        # Split when u need to
        num = arr[i]
        if num > stk[-1]:
            numstr = str(num)
            for j in range(len(numstr) - 1, -1, -1):
                stk.append(int(numstr[j]))
                
        else:
            stk.append(num)

    # Check if result is non decreasing
    for i in range(1, len(stk)):
        if stk[i] > stk[i-1]:
            print("NO")
            return
        
    print("YES")

main()