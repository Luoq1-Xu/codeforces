def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        n = int(input().strip())

        a = [int(i) for i in input().strip().split()]

        ans = 1
        curr = a[0]

        for i in range(1, len(a)):
            e = a[i]
            if e > curr + 1:
                ans += 1
                curr = e

        print(ans)



main()