import math

def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    n, m = (int(i) for i in input().strip().split())
    total_score = 0
    sums = []
    for i in range(n):
        arr = list(map(int, input().strip().split()))
        arr_score = 0
        running_sum = 0
        for e in arr:
            running_sum += e
            arr_score += running_sum

        sums.append(running_sum)
        total_score += arr_score
    
    sums.sort(reverse=True) # Arr with largest sum first
    for i in range(n):
        total_score += sums[i] * ((n - i - 1) * m)

    print(total_score)




main()