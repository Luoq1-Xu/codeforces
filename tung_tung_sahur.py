def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())
    for _ in range(lines):
        solve()


def solve():
    p = input().strip()
    s = input().strip()

    if len(s) > (2 * len(p)) or len(s) < len(p):
        print("NO")
        return

    ptr1 = 0
    char1 = p[ptr1]
    len1 = 0

    ptr2 = 0
    char2 = s[ptr2]
    len2 = 0

    while True:
        if char1 != char2:
            print("NO")
            return
        
        while ptr1 < len(p) and p[ptr1] == char1:
            ptr1 += 1
            len1 += 1

        while ptr2 < len(s) and s[ptr2] == char2:
            ptr2 += 1
            len2 += 1

        if len2 < len1 or len2 > (len1 * 2):
            print("NO")
            return
        
        if ptr1 >= len(p) and ptr2 >= len(s):
            break

        if ptr1 >= len(p) or ptr2 >= len(s):
            print("NO")
            return


        # Reset
        char1 = p[ptr1]
        char2 = s[ptr2]
        len1 = 0
        len2 = 0

    print("YES")

main()