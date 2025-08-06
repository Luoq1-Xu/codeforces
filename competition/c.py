def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1]) - 1

        heights = [int(i) for i in input().strip().split()]
        initial_height = heights[k]

        # To teleport successfully, height_diff <= curr_height - time
        heights.sort()
        i = heights.index(initial_height)

        can_reach = True

        # initial_height is the buffer - if any gap > initial_height, cannot reach the top
        while i < len(heights):
            if i > 0 and heights[i] - heights[i-1] > initial_height:
                can_reach = False
                break
            i += 1
        
        if can_reach:
            print("YES")
        else:
            print("NO")                


main()