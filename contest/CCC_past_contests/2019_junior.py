from collections import deque

def apply_rule(str, index, old, new):
    return str[:index] + new + str[index + len(old):]


def print_all_rules(final_str, rules_applied):
    for rule in rules_applied:



def j5():
    rules = [input(), input(), input()]
    rules = [rule.split() for rule in rules]

    transformation = input().split()
    num_subs, start, end = int(transformation[0]), transformation[1], transformation[2]

    # each item in deque is in the form (string, rules applied to get from start to string)
    # ex. if start = "ABAB", and rule 1 is "BA" -> "CC", we could have the item
    #  ("ACCB", [(1, 2)]) (1 means rule 1; 2 means on index 2 (strings are 1-indexed))
    q = deque([(start, [])])

    while q:
        cur_str, rules_applied = q.popleft()
        # try to find all cases where rules can be applied
        for rule_index in range(len(rules)):
            rule_old_sequence = rules[rule_index][0]
            rule_new_sequence = rules[rule_index][1]
            for string_index in range(len(cur_str) - len(rule_old_sequence) + 1):
                if cur_str[string_index:string_index + len(rule_old_sequence)] == rule_old_sequence:
                    new_str = apply_rule(cur_str, string_index, rule_old_sequence, rule_new_sequence)
                    new_rules_applied = rules_applied.copy()
                    new_rules_applied.append((rule_index + 1, string_index + 1))
                    if new_str == end:
                        print_all_rules(new_rules_applied)
                        return
                    q.append((new_str, [rule_index + 1, string_index + 1]))



