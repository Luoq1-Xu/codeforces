def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())

        if (n - 4) % 4 == 0:
            # Bob guaranteed to win, because every match he has an answer
            print("Bob")
        else:
            print("Alice")

main()