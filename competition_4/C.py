from collections import Counter

def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, k = (int(i) for i in input().strip().split())
        s = list(map(int, input().strip().split()))
        t = list(map(int, input().strip().split()))

        s_mods = Counter(e % k for e in s)

        possible = True
        for e in t:
            mod_class = e % k
            alt = (k - mod_class) % k

            if s_mods.get(mod_class, 0) > 0:
                s_mods[mod_class] -= 1
            elif s_mods.get(alt, 0) > 0:
                s_mods[alt] -= 1
            else:
                possible = False
                break
            
        if possible:
            print("YES")
        else:
            print("NO")
    
main()