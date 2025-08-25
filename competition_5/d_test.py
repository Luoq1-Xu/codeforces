def solve(k):
    # Helper function to calculate sum of digits in range [1, n]
    def digit_sum_1_to_n(n):
        if n <= 0:
            return 0
        
        s = str(n)
        m = len(s)
        total = 0
        
        # For each position from left to right
        for i in range(m):
            digit = int(s[i])
            left = int(s[:i]) if i > 0 else 0
            right_digits = m - i - 1
            
            # Numbers where current position < digit
            total += left * digit * (10 ** right_digits)
            
            # Numbers where current position = digit
            if i == m - 1:
                # Last position
                total += digit * (digit + 1) // 2
            else:
                right = int(s[i+1:]) if i < m - 1 else 0
                total += digit * (right + 1)
            
            # Sum contribution from positions to the right
            if right_digits > 0:
                total += left * 45 * (10 ** (right_digits - 1)) * right_digits
        
        return total
    
    # Find which number contains the k-th digit
    digits_used = 0
    digit_length = 1
    
    while True:
        # Count of numbers with 'digit_length' digits
        if digit_length == 1:
            count = 9
        else:
            count = 9 * (10 ** (digit_length - 1))
        
        total_digits = count * digit_length
        
        if digits_used + total_digits >= k:
            # The k-th digit is in a number with 'digit_length' digits
            remaining = k - digits_used
            
            # Which number in this group?
            num_index = (remaining - 1) // digit_length
            digit_index = (remaining - 1) % digit_length
            
            # The actual number
            if digit_length == 1:
                number = num_index + 1
            else:
                number = 10 ** (digit_length - 1) + num_index
            
            # Sum of all complete numbers before this one
            if number > 1:
                result = digit_sum_1_to_n(number - 1)
            else:
                result = 0
            
            # Add digits from the current number up to position digit_index
            num_str = str(number)
            for i in range(digit_index + 1):
                result += int(num_str[i])
            
            return result
        
        digits_used += total_digits
        digit_length += 1

# Read input and process test cases
t = int(input())
for _ in range(t):
    k = int(input())
    print(solve(k))