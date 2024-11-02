def s1():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))

    num_same_hat_opposite = 0
    for i in range(n//2):
        if l[i] == l[i + n // 2]:
            num_same_hat_opposite += 1

    print(num_same_hat_opposite * 2)


def is_alternating_light_heavy(s):
    letters_count = {}  # map from letter to count
    for letter in s:
        letters_count[letter] = letters_count.get(letter, 0) + 1

    last_heavy = None
    for letter in s:
        cur_letter_heavy = letters_count[letter] > 1
        if cur_letter_heavy == last_heavy:
            return False
        last_heavy = cur_letter_heavy

    return True


def s2():
    a = int(input().split()[0])
    for i in range(a):
        s = input()
        if is_alternating_light_heavy(s):
            print("T")
        else:
            print("F")


def s3():
    pass