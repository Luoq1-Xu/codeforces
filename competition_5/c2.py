def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    # Precalculate costs
    MAX_POWER = 21
    POWERS_OF_THREE = [1] * (MAX_POWER + 1)
    for i in range(1, MAX_POWER + 1):
        POWERS_OF_THREE[i] = POWERS_OF_THREE[i-1] * 3

    COSTS = [0] * MAX_POWER
    COSTS[0] = 3 # Cost of 1 watermelon
    for i in range(1, MAX_POWER):
        COSTS[i] = (POWERS_OF_THREE[i+1]) + (i * (POWERS_OF_THREE[i-1]))

    for _ in range(testcases):
        solve(COSTS)

def solve(COSTS):
    n, k = (int(i) for i in input().strip().split())

    # Convert to base 3 representation
    rem = []
    while n > 0:
        remainder = n % 3
        rem.append(remainder)
        n = n // 3

    min_deals = sum(rem)
    if k < min_deals:
        print(-1)
        return

    extra = k - min_deals # "buffer" that we have

    # As average cost always increases, we try to reduce the maximum first.
    # At any point in time, we can take 2 "reduces", and replace the largest deal with 3 deals than are 1 smaller
    # For example - lets say the largest element is 3^4
    # We can try to replace one 3^4 with 3 3^3, thus saving the maximum cost.

    reduces = extra // 2 # how many "reduces" we can do

    # Can't reduce beyond 1 watermelon
    for i in range(len(rem) - 1, 0, -1):
        if reduces == 0:
            break

        splits = min(reduces, rem[i])
        rem[i] -= splits
        rem[i-1] += 3 * splits
        reduces -= splits

    ans = 0
    for i in range(len(rem)):
        ans += rem[i] * COSTS[i]

    ans = int(ans) # min number of deals
    print(ans)

main()