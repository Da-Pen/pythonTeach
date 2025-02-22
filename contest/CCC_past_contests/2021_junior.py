from collections import deque

def books_sorted(books):
    cur_index = 0
    while cur_index < len(books) and books[cur_index] == "L":
        cur_index += 1
    while cur_index < len(books) and books[cur_index] == "M":
        cur_index += 1
    while cur_index < len(books) and books[cur_index] == "S":
        cur_index += 1

    return cur_index == len(books)


# swaps book at index i with book at index j. Assumption: i < j
# Ex. swap_books("LMS", 0, 2) -> "SML"
def swap_books(books, i, j):
    assert i < j and 0 <= i < len(books) and 0 <= j < len(books)
    return books[:i] + books[j] + books[i+1:j] + books[i] + books[j+1:]


# "SMLM" -> "LMSM"
#  |-> "MSLM" -> "LSMM" -> "LMMS"

def j4_brute_force():
    books = input()
    q = deque([(books, 0)])
    while q:
        cur_arrangement, num_swaps = q.popleft()
        if books_sorted(cur_arrangement):
            print(num_swaps)
            return

        # for each possible swap, add to queue
        for i in range(len(cur_arrangement)):
            for j in range(i + 1, len(cur_arrangement)):
                q.append((swap_books(cur_arrangement, i, j), num_swaps + 1))

    print("fail")




# "SML" -> "MSL" -> "SML" -> "MSL"

def j4_brute_force_v2():
    books = input()
    q = deque([(books, 0)])
    while q:
        cur_arrangement, num_swaps = q.popleft()
        if books_sorted(cur_arrangement):
            print(num_swaps)
            return

        # for each possible swap, add to queue
        for i in range(len(cur_arrangement)):
            for j in range(i + 1, len(cur_arrangement)):
                q.append((swap_books(cur_arrangement, i, j), num_swaps + 1))

    print("fail")







def j4_slightly_optimized():
    books = input()
    q = deque([(books, 0)])
    seen = set()
    while q:
        cur_arrangement, num_swaps = q.popleft()
        seen.add(cur_arrangement)
        if books_sorted(cur_arrangement):
            print(num_swaps)
            return

        # for each possible swap, add to queue
        for i in range(len(cur_arrangement)):
            for j in range(i + 1, len(cur_arrangement)):
                if cur_arrangement[i] != cur_arrangement[j]:
                    swapped = swap_books(cur_arrangement, i, j)
                    if swapped not in seen:
                        q.append((swapped, num_swaps + 1))

    print("fail")


# Idea: doing swaps in the following order will result in least # swaps:
# 1. Swap all S's into the S space.
#    - If there are S's in L space, swap it with L's where possible.
# 2. Swap the L's and M's in the wrong space
#
# Calculating # of swaps: Add these two numbers
#   (a) number of S's not in S space (we need a swap for each of them)
#   (b) number of swaps we have to do between L's and M's after we get all S's into place
# To calculate (b), we need to know how many L's are misplaced after we get all S's
# into place. This will be equal to:
#   number of misplaced L's - number of misplaced L's we can get into place from first step
# which is equal to:
#   number of misplaced L's - min(number of L's in S space, number of S's in L space)
# Therefore, the final calculation is
#   min_swaps = num_misplaced_S + num_misplaced_L - min(num_L_in_S_space, num_S_in_L_space)
def j4_best():
    books = input()
    # num_s = books.count("S")
    num_m = books.count("M")
    num_l = books.count("L")

    m_start_index = num_l
    s_start_index = m_start_index + num_m

    num_misplaced_S, num_misplaced_L = 0, 0
    num_L_in_S_space, num_S_in_L_space = 0, 0

    for i in range(len(books)):
        if books[i] == "S":
            if i < s_start_index:
                num_misplaced_S += 1
                if i < m_start_index:
                    num_S_in_L_space += 1
        if books[i] == "L":
            if i >= m_start_index:
                num_misplaced_L += 1
                if i >= s_start_index:
                    num_L_in_S_space += 1

    print(num_misplaced_S + num_misplaced_L - min(num_L_in_S_space, num_S_in_L_space))


# j4_best()


def j5():
    m = int(input())
    n = int(input())
    k = int(input())

    canvas = [[False for j in range(n)] for i in range(m)]
    for i in range(k):
        line = input().split()
        row_or_col, num = line[0], int(line[1]) - 1
        if row_or_col == "R":
            for j in range(n):
                canvas[num][j] = not canvas[num][j]
        else:
            for j in range(m):
                canvas[j][num] = not canvas[j][num]

    # count golds (True's)
    num_gold = 0
    for row in canvas:
        for cell in row:
            if cell:
                num_gold += 1

    print(num_gold)




