import heapq

def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n, l, r = (int(i) for i in input().strip().split())
    arr = list(map(int, input().strip().split()))

    # let x = num of elements in interval
    # Min value = min(min_sum of smallest x elements from 0 ... r, min_sum of smallest x elements from l ... n - 1)
    heap = [] # max_heap (we want the smallest elements)
    x = r - l + 1
    left_sum = 0
    right_sum = 0

    for i in range(r):
        e = arr[i]
        left_sum += arr[i]
        heapq.heappush(heap, -e)
        if len(heap) > x:
            to_remove = -heapq.heappop(heap)
            left_sum -= to_remove

    heap.clear()
    for i in range(l - 1, n):
        e = arr[i]
        right_sum += e
        heapq.heappush(heap, -e)
        if len(heap) > x:
            to_remove = -heapq.heappop(heap)
            right_sum -= to_remove

    print(min(left_sum, right_sum))
    

main()