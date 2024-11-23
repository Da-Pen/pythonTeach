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


j4()