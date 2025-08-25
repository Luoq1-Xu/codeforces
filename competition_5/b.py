def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())
    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())        
    suitable = []
    power = 1
    div = (1 + (10**power))

    while div <= n:
        if n % div == 0:
            suitable.append(str(n // div))

        power += 1
        div = (1 + (10**power))

    if not suitable:
        print(0)
        return

    print(len(suitable))
    print(" ".join(reversed(suitable))) 
    return

main()