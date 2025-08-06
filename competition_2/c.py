def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input())

        points = []
        for i in range(n):
            line = input().strip().split()
            x, y = int(line[0]), int(line[1])
            points.append((x, y, i + 1))  # Store i as point number

        # Find the two sets of points to pair first
        # We do this by sorting based on x
        # The first half are the x smallest points, the second half are the x largest points
        points.sort(key=lambda p: p[0])
        first_half = points[:n//2]
        second_half = points[n//2:]

        # Now, we must maximize y-coordinate differences by making pairs between the two halves
        # We do this by greedily pairing the smallest y with the largest y
        first_half.sort(key=lambda p: p[1]) # Sort first half ascending
        second_half.sort(key=lambda p: p[1], reverse=True) # Sort second half descending

        # Greedy pairing
        pairs = []
        for i in range(n//2):
            pairs.append((first_half[i][2], second_half[i][2])) # Get point numbers

        # Output the pairs
        for a, b in pairs:
            print(a, b)

main()