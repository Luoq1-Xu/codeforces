def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    # Min cost == least switches
    n = int(input().strip())
    string = input().strip()

    switches = 0 if string[0] == "0" else 1
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            switches += 1

    if switches > 2:
        switches -= 2
    elif switches == 2:
        switches -= 1

    print(n + switches)

main()