def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, m = (int(i) for i in input().strip().split())

        matrix = [[] for _ in range(n)]

        max_val = float("-inf")
    
        # Read in the matrix
        for i in range(n):
            matrix[i] = [int(j) for j in input().strip().split()]
            line_max = max(matrix[i])
            max_val = max(max_val, line_max)

        can_lower = True # Can we lower the minimum max by 1?
        points = []

        # Find num of ocurrences of max val in rows and cols
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == max_val:   
                    points.append((i,j))

        if points:
            x, y = points[0]

            # Hypothesis 1: x == the row, do all non x row have the same col?
            col = set()
            hypo_1 = True
            for point in points:
                if point[0] != x:
                    col.add(point[1])
                    if len(col) > 1:
                        hypo_1 = False
                        break

            if not hypo_1:
                # Hypo 2: y == the col, do all non y col have the same row x?
                row = set()
                for point in points:
                    if point[1] != y:
                        row.add(point[0])
                        if len(row) > 1:
                            can_lower = False
                            break            

        if can_lower:
            print(max_val - 1)
        else:
            print(max_val)

main()