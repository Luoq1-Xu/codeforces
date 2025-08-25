def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, k = (int(i) for i in input().strip().split())
        s = list(map(int, input().strip().split()))
        t = list(map(int, input().strip().split()))

        for i in range(n):
            s[i] = min(s[i] % k, k - (s[i] % k))

        for j in range(n):
            t[j] = min(t[j] % k, k - (t[j] % k))

        if sorted(s) == sorted(t):     
            print("YES")
        else:
            print("NO")
    
main()