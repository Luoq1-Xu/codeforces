def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        solve()

def solve():
    n = int(input().strip()) 
    line = input().strip()

    def beats(x, y):
        # Does x beat y?
        if x == 0 and y == n - 1:
            return True
        if x == n - 1 and y == 0:
            return False
        return x > y

    # Whoever wins the first turn is guaranteed to win
    alice_can_win = False
    for i in range(len(line)):
        if line[i] != "A":
            continue # Don't care
    
        # Check if can beat
        can_beat = True
        for j in range(n):
            # Check if can beat every bob card
            if line[j] == "B" and not beats(i, j):
                can_beat = False
                break
        if can_beat:
            alice_can_win = True
            break

    if alice_can_win:
        print("Alice")
    else:
        print("Bob")

main()