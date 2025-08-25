from collections import deque
def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())
    a = input().strip()
    m = int(input().strip())
    b = input().strip()
    c = input().strip()

    res = deque(a.split())
    for i in range(m):
        if c[i] == 'V':
            res.appendleft(b[i])
        else:
            res.append(b[i])

    print("".join(res))



main()