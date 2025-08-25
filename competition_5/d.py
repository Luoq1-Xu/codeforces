def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())
    for _ in range(testcases):
        solve()

def solve():
    # Block 1 -> 1-9 (size = 9, digits = 9) sum of digits = 45
    # Block 2 -> 10-99 (size = 90, digits = 90 * 2 = 180) sum of digits => 10 of every digit = 45 * 10 + (45 * 9)
    # Block 3 -> 100-999 (size = 900, digits = 900 * 3 = 2700)
    # Block 4 -> 1000-9999 (size = 9000, digits = 9000 * 4 = 36000)
    # and so on, so forth
    # Keep dividing by blocks until cannot

    # For every block, sum of digits = digit_count * (45 * 10**(digit_count - 1)) - previous blocks sums

    k = int(input().strip())

    ans = 0
    digits = 1
    prev_sums = 0
    while True:
        block_size = 9 * (10**(digits-1))
        block_digits_total = block_size * digits

        if k < block_digits_total:
            # Cannot include whole block
            break
        else:
            # Include the whole block
            sum_of_digits = digits * 45 * (10**(digits-1))
            sum_of_digits -= prev_sums
            ans += sum_of_digits
            prev_sums += sum_of_digits
            digits += 1
            k -= block_digits_total

    # Process remaining
    start = (10**(digits-1))
    full_nums = (k-1) // digits

    for i in range(full_nums):
        for j in str(i):
            ans += int(j)
    
    # Last, possibly partial num
    digits_left = (k-1) % digits + 1
    num = str(start + full_nums) # Last number

    for i in range(digits_left):
        ans += int(num[i])

    print(ans)
    return
            


        




main()