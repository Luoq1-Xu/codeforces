import sys

# It's good practice in competitive programming to use fast I/O in Python.
def fast_input():
    return sys.stdin.readline().rstrip()

def add_to_basis(basis, val):
    """
    Adds a value to the basis.
    It reduces the value by the existing basis vectors. If the value is still
    non-zero, it's added to the basis, maintaining the basis property.
    """
    for basis_vec in basis:
        val = min(val, val ^ basis_vec)
    if val > 0:
        basis.append(val)
        # Sorting isn't strictly required for correctness but keeps the
        # basis in a canonical form and can be slightly faster for reduction.
        basis.sort(reverse=True)

def can_form(basis, val):
    """
    Checks if a value can be formed by XORing elements of the basis.
    This is true if the value can be reduced to 0 by the basis vectors.
    """
    for basis_vec in basis:
        val = min(val, val ^ basis_vec)
    return val == 0

def solve():
    """
    Solves a single test case.
    """
    try:
        n = int(fast_input())
        a = list(map(int, fast_input().split()))
        b = list(map(int, fast_input().split()))
    except (IOError, ValueError):
        return

    # Condition 1: The last element is immutable.
    if a[-1] != b[-1]:
        print("NO")
        return

    basis = []
    # The value a[n-1] is the first element available to form XOR sums.
    add_to_basis(basis, a[-1])

    # Iterate backwards from the second-to-last element.
    for i in range(n - 2, -1, -1):
        # The required_xor is the value 'x' such that a[i] ^ x = b[i].
        # So, x = a[i] ^ b[i].
        required_xor = a[i] ^ b[i]

        if required_xor == 0:
            # a[i] is already equal to b[i]. No operation needed at this step.
            # However, the original a[i] is now available for operations at indices < i.
            add_to_basis(basis, a[i])
        else:
            # We must perform the operation. We need to check if we can form
            # the required_xor value from the numbers to the right of i.
            if can_form(basis, required_xor):
                # If it's possible, add the original a[i] to the basis
                # for subsequent steps.
                add_to_basis(basis, a[i])
            else:
                # If we cannot form the required value, the transformation is impossible.
                print("NO")
                return

    # If the loop completes, it means a valid sequence of operations exists for every element.
    print("YES")

def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(fast_input())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()