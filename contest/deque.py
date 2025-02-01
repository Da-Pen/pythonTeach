from collections import deque

def is_palindrome(s):
    dq = deque(s)
    while dq:
        l = dq.popleft()
        if not dq:
            return True
        r = dq.pop()
        if l != r:
            return False
    return True

print(is_palindrome("racecar"))


def reverse_first_k_elements(dq, k):
    dq2 = deque()
    for _ in range(k):
        dq2.append(dq.popleft())

    for _ in range(k):
        dq.appendleft(dq2.popleft())

dq = deque([1, 2, 3, 4, 5])
reverse_first_k_elements(dq, 3)
print(dq)


