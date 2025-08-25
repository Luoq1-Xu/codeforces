import heapq

def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    # Find k + 1 largest non consecutive elements
    n, k = (int(i) for i in input().strip().split())
    arr = list(map(int, input().strip().split()))

    if n == k + 1:
        print(sum(arr))
        return
    
    heap = []
    largest_sum = 0
    max_element = -1
    # min heap, stores k + 1 largest elements
    for e in arr:
        max_element = max(max_element, e)
        largest_sum += e
        heapq.heappush(heap, e)
        if len(heap) > k + 1:
            smallest = heapq.heappop(heap)
            largest_sum -= smallest

    # If k >= 2, guaranteed to be able to make this largest sum
    # Just take k elements with a gap in the middle
    # You will always be able to leave that gap to the very last
    if k >= 2:
        print(largest_sum)
        return 
    
    # However, if k == 1, then your job is to see if:
    # You take the max element, then the start or end
    print(max(arr[-1] + max(arr[:-1]), (arr[0] + max(arr[1:]))))
    return

main()