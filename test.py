def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])
        array = [int(i) for i in input().strip().split()]

        # Find the longest consecutive of (k * 0 + any digit)
        longest = 0
        counter = 0
        for num in array:
            if num == 1:
                if counter == k:
                    longest += 1
                # Reset counter
                counter = 0
            else:
                if counter == k:
                    # Rest day, reset
                    counter = 0
                    longest += 1
                    continue
                counter += 1
        if counter == k:
            longest += 1
        print(longest)

main()