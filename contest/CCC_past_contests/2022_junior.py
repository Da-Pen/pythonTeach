def j3():
    pass  # TODO

def j4():  # also s2
    num_same_group_constraints = int(input())
    same_group_constraints = set()
    for _ in range(num_same_group_constraints):
        p1, p2 = sorted(input().split())
        same_group_constraints.add((p1, p2))

    num_diff_group_constraints = int(input())
    diff_group_constraints = set()
    for _ in range(num_diff_group_constraints):
        p1, p2 = sorted(input().split())
        diff_group_constraints.add((p1, p2))

    num_groups = int(input())
    num_diff_group_constraints_violated = 0
    num_same_group_constraints_satisfied = 0

    for _ in range(num_groups):
        members = sorted(input().split())
        if (members[0], members[1]) in same_group_constraints:
            num_same_group_constraints_satisfied += 1
        if (members[0], members[2]) in same_group_constraints:
            num_same_group_constraints_satisfied += 1
        if (members[1], members[2]) in same_group_constraints:
            num_same_group_constraints_satisfied += 1

        if (members[0], members[1]) in diff_group_constraints:
            num_diff_group_constraints_violated += 1
        if (members[0], members[2]) in diff_group_constraints:
            num_diff_group_constraints_violated += 1
        if (members[1], members[2]) in diff_group_constraints:
            num_diff_group_constraints_violated += 1

    print(num_diff_group_constraints_violated
          + (num_same_group_constraints - num_same_group_constraints_satisfied))


def j5():
    '''
    Not the most efficient implementation. More efficient would be a quadtree,
    but that's very advanced.
    '''
    n = int(input())
    num_trees = int(input())

    # map of key -> set of cols
    # Ex 0 0 0 0
    #    1 0 0 1
    #    0 1 1 1
    #
    #    {1: set(0, 3), 2: set(1, 2, 3)}
    trees_by_row = {}
    for t in range(num_trees):
        line = input().split(" ")
        x, y = int(line[0]) - 1, int(line[1]) - 1
        if x not in trees_by_row:
            trees_by_row[x] = set()
        trees_by_row[x].add(y)

    for pool_size in range(n, 0, -1):
        for start_row in range(n - pool_size + 1):
            for start_col in range(n - pool_size + 1):
                valid = True  # whether a pool of size pool_size starting at (start_row, start_col) would fit on the grid without trees
                for x in range(start_row, start_row + pool_size):
                    for y in range(start_col, start_col + pool_size):
                        if x in trees_by_row and y in trees_by_row[x]:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    return pool_size

    return 0  # completely covered by trees


print(j5())