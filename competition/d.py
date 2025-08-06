def main():
    import sys
    import bisect
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        line = input().strip().split()
        n, k = int(line[0]), int(line[1])

        casinos = []
        for i in range(n):
            raw = input().strip().split()
            l, r, real = int(raw[0]), int(raw[1]), int(raw[2])
            casinos.append((l, r, real))

        casinos.sort(key=lambda x: (x[0], x[2])) # Sort by l then real

        ptr = 0
        max_earnings = k
        max_seen = 0 # Max
        while ptr < len(casinos):
            casino = casinos[ptr]
            if casino[0] > max_earnings:
                # Entry fee too high
                max_earnings = max(max_seen, max_earnings)

                # If still too high, quit, already attained highest earnings
                if casino[0] > max_earnings:
                    break
            
            max_seen = max(max_seen, casinos[ptr][2])
            ptr += 1
        
        max_earnings = max(max_earnings, max_seen)
        print(max_earnings)

main()