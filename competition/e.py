def main():
    import sys
    from math import gcd
    input = sys.stdin.readline

    num_cases = int(input())

    for _ in range(num_cases):
        n = int(input())
        
        p = [int(i) for i in input().strip().split()]
        s = [int(i) for i in input().strip().split()]

        is_valid = True
        gcd_of_whole_array = s[0]

        if s[0] != p[-1]:
            print("NO") # Not aligned
            continue

        # Check if p is valid
        for i in range(1, n):
            if p[i-1] % p[i] != 0:
                is_valid = False
                break

        for j in range(n-2, -1, -1):
            if s[j+1] % s[j] != 0:
                is_valid = False
                break

        # Check if both align
        for x in range(1, n):
            if gcd(p[x-1], s[x]) != gcd_of_whole_array:
                is_valid = False
                break

        if is_valid:
            print("YES")
        else:
            print("NO")

main()