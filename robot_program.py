def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        n, x, k = (int(i) for i in input().strip().split())
        inst = input().strip()
        solve(n, x, k, inst)

def solve(n, x, k, inst):

    net_moves = 0

    moves_to_reset = None # If reached zero, will keep looping for this amount of moves
    reached_zero_turn = -1

    for i in range(n):
        c = inst[i]
        if c == "L":
            net_moves -= 1
            x -= 1
        else:
            net_moves += 1
            x += 1
        if net_moves == 0 and not moves_to_reset:
            moves_to_reset = i + 1

        if x == 0 and reached_zero_turn == -1:
            reached_zero_turn = i + 1 # Reached zero on this turn

    if reached_zero_turn == -1:
        # Cannot reach 0
        print(0)
        return

    # Otherwise, it reaches zero
    if not moves_to_reset:
        print(1)
        return # Reaches zero once and never again
    
    # Can loop, calculate how many times can loop
    print(1 + ((k - reached_zero_turn) // moves_to_reset))
        

main()