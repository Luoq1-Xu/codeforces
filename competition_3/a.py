def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        line = input().strip()

        f_chars = 0
        t_chars = 0
        n_chars = 0
        assorted = []

        for c in line:
            if c == "F":
                f_chars += 1
            elif c == "T":
                t_chars += 1
            elif c == "N":
                n_chars += 1
            else:
                assorted.append(c)

        ans = []

        for _ in range(t_chars):
            ans.append("T")

        for _ in range(f_chars):
            ans.append("F")

        for _ in range(n_chars):
            ans.append("N")

        ans.extend(assorted)

        print("".join(ans))
                

main()