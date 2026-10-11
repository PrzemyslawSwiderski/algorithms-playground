#!/usr/bin/env python3
from collections import defaultdict

# https://www.hackerrank.com/challenges/cut-the-tree/problem
def cutTheTree(data, edges):
    n = len(data)

    # ------------------------------------------------------------------
    # STEP 1: Total sum of all node values.
    #
    # Key insight: if we cut an edge, the tree splits into two parts.
    # If one part has sum S, the other part has sum (total - S).
    # The difference we want to minimize is:
    #     |S - (total - S)|  =  |total - 2*S|
    # So we never need to compute BOTH parts — knowing S is enough.
    # ------------------------------------------------------------------
    total = sum(data)
    print(f"Total sum of all nodes: {total}")

    # ------------------------------------------------------------------
    # STEP 2: Build an adjacency list.
    #
    # The edges are undirected, so each edge (u, v) must be recorded
    # in BOTH directions: v is reachable from u, and u from v.
    # ------------------------------------------------------------------
    adjacency = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    print("Adjacency list:")
    for node in sorted(adjacency):
        print(f"  node {node} -> connected to {adjacency[node]}")

    # ------------------------------------------------------------------
    # STEP 3: Pick an arbitrary root (node 1) and traverse the tree.
    #
    # This DFS does NOT compute subtree sums yet. It only:
    #   a) records the parent of every node, and
    #   b) records the order in which nodes were visited (pre-order).
    #
    # "Pre-order" means: a parent always appears BEFORE its children
    # in the `order` list. That property is what makes STEP 4 work.
    #
    # We use an explicit stack instead of recursion, because Python's
    # default recursion limit (~1000) would crash on deep trees.
    # ------------------------------------------------------------------
    ROOT = 1
    parent = [0] * (n + 1)  # parent[k] = parent node of node k
    visited = [False] * (n + 1)  # avoid going back where we came from
    order = []  # nodes in DFS pre-order

    stack = [ROOT]
    visited[ROOT] = True
    parent[ROOT] = 0  # the root has no parent

    while stack:
        node = stack.pop()
        order.append(node)  # record visit order
        for neighbor in adjacency[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node  # we arrived here FROM `node`
                stack.append(neighbor)

    print(f"DFS visit order (pre-order): {order}")

    # ------------------------------------------------------------------
    # STEP 4: Compute the subtree sum for EVERY node at once.
    #
    # subtree[k] = sum of data values of node k and ALL its descendants.
    #
    # Trick: we walk the visit order BACKWARDS (children before parents,
    # guaranteed by pre-order). When we process a child, we "push" its
    # accumulated sum up into its parent. By the time the parent is
    # processed, all its children have already added their sums in.
    #
    # Initialize: each node starts with its own value.
    # ------------------------------------------------------------------
    subtree = [0] * (n + 1)
    for node in range(1, n + 1):
        subtree[node] = data[node - 1]

    # Then accumulate children into parents, deepest first.
    for node in reversed(order):
        root = parent[int(node)]
        if root != 0:  # skip the root (no parent)
            subtree[root] += subtree[node]
            print(f"  pushed sum of subtree({node}) = {subtree[node]} "
                  f"up into node {root}")

    print("Subtree sums:")
    for node in range(1, n + 1):
        print(f"  subtree({node}) = {subtree[node]}")

    # ------------------------------------------------------------------
    # STEP 5: Try every possible cut.
    #
    # Cutting the edge between node k and its parent detaches the
    # subtree rooted at k. So:
    #   - part 1 sum = subtree[k]
    #   - part 2 sum = total - subtree[k]
    #   - difference = |total - 2 * subtree[k]|
    #
    # Every node except the root corresponds to exactly one edge,
    # so we simply check all of them and keep the minimum.
    # ------------------------------------------------------------------
    min_diff = float('inf')
    best_node = None

    for node in order:
        if node == ROOT:
            continue  # the root's "subtree" is the whole tree — not a cut

        diff = abs(total - 2 * subtree[node])
        print(f"Cut above node {node}: subtree sum = {subtree[node]}, "
              f"other side = {total - subtree[node]}, diff = {diff}")

        if diff < min_diff:
            min_diff = diff
            best_node = node

    print(f"Best cut: edge above node {best_node}, difference = {min_diff}")
    return min_diff


if __name__ == '__main__':
    data = [100, 200, 100, 500, 100, 600]
    edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
    result = cutTheTree(data, edges)
    print(f"\n{result=}")
