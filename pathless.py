def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, s = (int(i) for i in input().strip().split())
        arr = list(map(int, input().strip().split()))
        solve(n, s, arr)

def solve(n, s, arr):
    total = sum(arr)

    if s < total:
        # Can never make the ans
        print(" ".join(list(map(str, arr))))
        return
    
    if s == total or s - total > 1:
        # Can always make the ans
        print(-1)
        return
    
    # If diff is 1, make sure this is unachieveable, then can block alice
    counts = [0] * 3
    for e in arr:
        counts[e] += 1

    ans = []
    # Put all the zeroes first
    for _ in range(counts[0]):
        ans.append("0")
    
    # Put all the 2s next
    for _ in range(counts[2]):
        ans.append("2")

    # Put the ones last
    for _ in range(counts[1]):
        ans.append("1")

    print(" ".join(ans))
    return
    

    


    



main()