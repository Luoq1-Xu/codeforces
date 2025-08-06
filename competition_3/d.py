def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        l, r = (int(i) for i in input().strip().split())
        print(good_from_1_to_n(r) - good_from_1_to_n(l-1)) # l - 1 because we don't want to include l in the lower range

def good_from_1_to_n(n):
    possible = n # Total possible candidates initially

    not_good = 0 # All numbers that cannot be good (divisible by 1 or more of the single primes)

    # Form the count of not good numbers
    not_good = (possible // 2 + possible // 3 + possible // 5 + possible // 7) # Divisible by single prime

    # We double subtracted some numbers
    # Those numbers divisible by any combination of 2 of these primes (e.g. divisible by 2 and 3) must be added back
    not_good -= (possible // 6 + possible // 10 + possible // 14 + possible // 15 + possible // 21 + possible // 35)

    # But now some numbers added back too many times, need to subtract again, so they end up as -1 nett
    # These numbers have 3 factors out of 2, 3, 5, 7
    not_good += (possible // 30 + possible // 42 + possible // 70  + possible // 105)

    # Then we add back those numbers that divisible by all 2, 3, 5 and 7
    not_good -= (possible // 210)

    # Example: 210
    # 1st step: -4 net
    # 2nd step: +2 net
    # 3rd step: -2 net
    # 4th step: -1 net

    return possible - not_good


main()