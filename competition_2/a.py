def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        line = input().strip().split()
        n, m = int(line[0]), int(line[1])       

        if n == 1 or m == 1:
            print("NO") # Impossible since any path would be greedy
            continue

        if n == 2 and m == 2:
            print("NO")
            continue
    
        print("YES")        

main()