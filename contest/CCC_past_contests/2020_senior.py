from collections import defaultdict

# dict1 can have key-value pairs where the value is the default-value of dict2
# ex. if dict1 = {"a": 0, "b": 1, "c": 2} and dict2 = {"b": 1, "c": 2}
# Then this will return True
def dict_equals(dict1, dict2):
    for k in dict1:
        if dict1[k] != dict2[k]:
            return False
    return True

def s3():
    n = input()
    h = input()

    n_letter_counts = defaultdict(int)
    for letter in n:
        n_letter_counts[letter] += 1

    # sliding window over haystack
    h_window_letter_counts = defaultdict(int)
    for i in range(len(n)):
        h_window_letter_counts[h[i]] += 1

    # abcdef
    # abc

    found_permutations = set()
    for start_letter_index in range(len(h) - len(n) + 1):
        # don't need to update h_window_letter_counts on first loop; otherwise update it for new window
        if start_letter_index != 0:
            h_window_letter_counts[h[start_letter_index - 1]] -= 1
            h_window_letter_counts[h[start_letter_index + len(n) - 1]] += 1
        if dict_equals(h_window_letter_counts, n_letter_counts):
            found_permutations.add(h[start_letter_index:start_letter_index + len(n)])

    print(len(found_permutations))

s3()
