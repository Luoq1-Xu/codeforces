def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    n, k = (int(i) for i in input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    min_a = float("inf")
    max_a = float("-inf")
    x = None

    for i in range(n):
        min_a = min(min_a, a[i])
        max_a = max(max_a, a[i])

        if x != None and b[i] != -1 and a[i] + b[i] != x:
            print(0) # Impossible
            return
        
        if b[i] != -1 and x == None:
            x = a[i] + b[i]

    if x != None and max_a > x:
        print(0)
        return
    
    if x != None and min_a + k < x:
        # Impossible to satisfy
        print(0)
        return
    
    if x != None:
        print(1) # Only one possible way
        return
    
    ans = (k + min_a) - max_a + 1

    if ans <= 0:
        print(0)
    else:
        print(ans)


main()