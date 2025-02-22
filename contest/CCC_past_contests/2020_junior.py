
def is_cyclic_shift(a, b):
    if len(a) != len(b):
        return False
    # Look for letters in b that are the starting letter of a.
    # For each one, check if it's a cycle of a.
    for i in range(len(b)):
        if b[i] == a[0]:
            num_letters_right = len(b) - i  # number of letters from b[i] to the end of b (inclusive)
            if b[i:] == a[:num_letters_right] and b[:i] == a[num_letters_right:]:
                return True

    return False


def j3():
    t = input()
    s = input()
    for i in range(len(t) - len(s) + 1):
        if is_cyclic_shift(t[i:i + len(s)], s):
            print("yes")
            return
    print("no")

j3()


