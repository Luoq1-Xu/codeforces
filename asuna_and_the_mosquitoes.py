import heapq

def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    even_cnt = 0
    odd_cnt = 0

    max_even = 0
    max_odd = 0
    total_sum = 0

    for e in arr:
        total_sum += e
        if e % 2:
            odd_cnt += 1
            max_odd = max(max_odd, e)
        else:
            even_cnt += 1
            max_even = max(max_even, e)

    if even_cnt == 0:
        print(max_odd)
        return
    
    if odd_cnt == 0:
        print(max_even)
        return

    print(total_sum - (odd_cnt - 1))
    return

main()