def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        n = int(input().strip())

        print(2 * n - 1)
        for i in range(n):
            print(i+1, 1, i+1)
            if (i+2 <= n):
                print(i+1, i+2, n)

main()