def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        n, j, k = (int(i) for i in input().strip().split())

        players = [int(i) for i in input().strip().split()]
        max_strength = max(players)

        j_strength = players[j-1] # 0 indexed

        if k == 1 and j_strength == max_strength:
            # To be the last one standing, must be strongest (or tied strongest)
            print("YES")
            continue

        if k >= 2:
            # Always possible, since can always eliminate other ppl
            print("YES")
            continue

        # Otherwise, means k == 1 and not strongest, impossible
        print("NO")


main()