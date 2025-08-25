def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip())
    px, py, qx, qy = (int(i) for i in input().strip().split())
    arr = list(map(int, input().strip().split()))

    # Maximum possible distance we can be from starting point after all operations
    max_dist = sum(arr)

    # Min possible distance
    # Since we are on a 2d plane, 
    # The remaining moves (other than the longer moves)
    # Can be combined in a way to reach back
    longest_seg = max(arr)
    min_dist = max(longest_seg - (max_dist - longest_seg), 0)

    # Check if new dist between start and end is within this range
    dist = (((qx - px)**2) + ((qy - py)**2))**(1/2)

    if min_dist <= dist <= max_dist:
        print("YES")
    else:
        print("NO")


main()