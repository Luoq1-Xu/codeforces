def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n = int(input())

        total_moves = 0

        for _ in range(n):
            line = input().strip().split()
            a, b, c, d = int(line[0]), int(line[1]), int(line[2]), int(line[3])

            # Any extra elements in initial that are not in target need to be moved away
            zeroes_to_move = max(0, a - c)

            # Count how many "blocking zeroes" (zeroes that block the ones from being given away)
            # If we can offset these with zeroes we needed to move anyway, then no extra moves needed
            # Because moving those zeroes would be counted in misplaced
            # Otherwise, we need to swap them out
            ones_to_move = max(0, b - d)
            if ones_to_move > 0:
                # Additional moves incurred due to "wasted" moves just to bubble up the ones
                blocking_zeroes = a - zeroes_to_move 
                total_moves += zeroes_to_move + ones_to_move + blocking_zeroes
            else:
                total_moves += zeroes_to_move # Otherwise, we just need to move the zeroes
            
        print(total_moves)

main()