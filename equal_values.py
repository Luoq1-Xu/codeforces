def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        line = list(map(int, input().strip().split()))
        n, m = line[0], line[1]
        x, y = line[2], line[3]

        # num of turns = num of row cuts + num of col cuts
        directions = [
            (x, m), # left cut
            (n - x + 1, m), # right cut
            (n, y), # top cut
            (n, m - y + 1) # bottom cut
        ]

        ans = n + m  # Worst case = n vertical cuts and m horizontal cuts
        for a, b in directions:
            res = 0
            while (a > 1):
                res += 1
                a = (a + 1) // 2
            while (b > 1):
                res += 1
                b = (b + 1) // 2
            ans = min(ans, res)

        print(1 + ans)

main()