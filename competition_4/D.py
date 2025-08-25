def main():
    import sys
    input = sys.stdin.readline

    testcases = int(input())

    for _ in range(testcases):
        # Minimum diameter = 2
        # How many operations to turn graph into one parent (star graph)?

        n = int(input().strip())
        adj_list = [[] for _ in range(n + 1)] # 1-indexed
        for _ in range(n - 1):
            u, v = (int(i) for i in input().strip().split())
            adj_list[u].append(v)
            adj_list[v].append(u)


def num_of_leaves(node, adj_list):
    if len(adj_list[node]) == 1:
        # is leaf node
        return 1
    
    








main()