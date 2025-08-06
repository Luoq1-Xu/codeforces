def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    """
    Jerry only ever wins if:
    1. Tom lost by default (first round diff > k no matter what move)
    2. Wins eventually: even number of boxes total
    """
    n, k = (int(i) for i in input().strip().split())
    arr = list(map(int, input().strip().split()))

    total = 0
    largest = arr[0]
    smallest = arr[0]

    largest_count = 0
    smallest_count = 0

    for num in arr:
        total += num
        if num > largest:
            largest = num
            largest_count = 1
        elif num == largest:
            largest_count += 1

        if num < smallest:
            smallest = num
            smallest_count = 1
        elif num == smallest:
            smallest_count += 1

    if largest - smallest > k + 1:
        print("Jerry")
        return
    
    if largest - smallest > k and largest_count > 1:
        print("Jerry")
        return
    
    if total % 2:
        print("Tom")
    else:
        print("Jerry")

main()