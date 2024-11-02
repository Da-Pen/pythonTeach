
def j1():
    num_red = int(input())
    num_green = int(input())
    num_blue = int(input())

    print((3 * num_red) + (4 * num_green) + (5 * num_blue))


def j2():
    dusa_size = int(input())
    while True:
        next_yobi_size = int(input())
        if next_yobi_size >= dusa_size:
            print(dusa_size)
            return
        dusa_size += next_yobi_size


def j3():
    all_scores = {}  # dictionary: score -> # participants with that score
    num_participants = int(input())
    for p in range(num_participants):
        p_score = int(input())
        all_scores[p_score] = 1 + all_scores.get(p_score, 0)

    # convert to list and sort
    all_scores_list = list(all_scores.keys())
    all_scores_list.sort(reverse=True)
    bronze_score = all_scores_list[2]

    print(bronze_score, all_scores[bronze_score])


def j4():
    word_normal = input() + "-"
    word_weird = input() + "-"

    i, j = 0, 0

    silly_key = '-'
    silly_key_replacement = '-'
    quiet_key = '-'

    while i < len(word_normal) and j < len(word_weird):
        if word_normal[i] == word_weird[j]:
            i += 1
            j += 1
            continue

        # Example: o replaced with x
        # ooooaaaa
        # xxxxaaaa

        # Example: a is quiet, o replaced with x
        # aaaabco
        # bcx

        # Observation: if the letter's don't match, then a forward search will reveal that the next
        # different letter in the "normal" word is equal to the replacement letter of the "weird" word

        next_different_letter_index = i
        while word_normal[i] == word_normal[next_different_letter_index]:
            next_different_letter_index += 1

        if word_weird[j] == word_normal[next_different_letter_index]:
            # we have found a quiet key
            quiet_key = word_normal[i]
            i = next_different_letter_index
        else:
            # we have found a replacement key
            silly_key = word_normal[i]
            silly_key_replacement = word_weird[j]
            i += 1
            j += 1

    print(silly_key, silly_key_replacement)
    print(quiet_key)


from collections import deque


def j5():
    num_rows = int(input())
    num_cols = int(input())
    grid = []

    # read input
    for row in range(num_rows):
        grid.append(input())

    farmer_row = int(input())
    farmer_col = int(input())
    farmer_start = (farmer_row, farmer_col)
    seen = set()
    seen.add(farmer_start)
    queue = deque()
    queue.append(farmer_start)

    total_value = 0

    while len(queue) > 0:
        node = queue.popleft()
        node_value = grid[node[0]][node[1]]
        if node_value == "*":  # bay of hale
            continue
        elif node_value == "S":
            total_value += 1
        elif node_value == "M":
            total_value += 5
        else:
            total_value += 10
        neighbours = ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1]))
        for neighbour in neighbours:
            if neighbour[0] < 0 or neighbour[0] >= num_rows or neighbour[1] < 0 or neighbour[1] >= num_cols:
                continue
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)

    print(total_value)
