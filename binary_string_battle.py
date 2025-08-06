def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        first_line = [int(i) for i in input().strip().split()]
        n, k = first_line[0], first_line[1]

        bin_string = input().strip()
        ones_count = 0

        # Count number of 1s in bin string
        for i in range(len(bin_string)):
            if bin_string[i] == "1":
                ones_count += 1
            
        # Alice auto-win condition
        if ones_count <= k:
            print("Alice")
            continue

        # Bob auto win condition (because bob can always "defend")
        if n >= (2 * k):
            print("Bob")
            continue

        # Otherwise, alice can eventually win, by forcing a 1 in the winning zone
        # Such that whatever move bob makes, he cannot get > k 1s back 
        print("Alice")

main()