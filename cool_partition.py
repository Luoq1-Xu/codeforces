def main():
    import sys
    input = sys.stdin.readline

    lines = int(input().strip())

    for _ in range(lines):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))

        freq = [0] * (n+1)
        distinct_at_i = [0] * n

        for i in range(n):
            freq[a[i]] += 1
            if (freq[a[i]] == 1):
                distinct_at_i[i] = 1
            distinct_at_i[i] += distinct_at_i[i-1] if i > 0 else 0

        # Reset freq
        for i in range(n+1):
            freq[i] = 0


        # Greedily partition whenever possible
        ans = 0
        end = n - 1
        unique = 0
    
        # Last segment must contain all unique elements (un-partitionable)
        for i in range(n - 1, -1, -1):
            freq[a[i]] += 1
            if (freq[a[i]] == 1):
                unique += 1

            if unique == distinct_at_i[end]:
                ans += 1
                 # Reset freq
                for j in range(i, end + 1):
                    freq[a[j]] = 0
                end = i - 1
                unique = 0

        print(ans)


main()