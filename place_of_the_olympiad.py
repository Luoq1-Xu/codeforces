import math

def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    n, m, k = (int(i) for i in input().strip().split())

    # Find maximum number of desks to accomodate per row
    max_desks = math.ceil(k / n)

    # Find number of empty spots -> this dictates how many groups we can split
    empty = m - max_desks

    # Find the minimum longest bench
    longest = math.ceil(max_desks / (empty + 1))

    print(longest)

main()