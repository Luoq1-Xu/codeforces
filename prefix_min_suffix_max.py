def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input().strip())
        ans = []
        line = [int(i) for i in input().strip().split()]
        
        smallest_to_the_left = [0] * n
        largest_to_the_right = [0] * n

        # Populate smallest to the left
        curr_smallest = float('inf')
        for i in range(n):
            smallest_to_the_left[i] = curr_smallest
            curr_smallest = min(curr_smallest, line[i])

        # Populate largest to the right
        curr_largest = float('-inf')
        for i in range(n-1, -1, -1):
            largest_to_the_right[i] = curr_largest
            curr_largest = max(curr_largest, line[i])


        for i in range(n):
            # Only possible scenario where impossible:
            # Smallest on the left is smaller than u
            # and largest on the right is larger than u
            # Means u will eventually get absorbed, cannot be last one standing
            if smallest_to_the_left[i] < line[i] < largest_to_the_right[i]:
                ans.append("0")
            else:
                ans.append("1")
                
        print("".join(ans))

main()