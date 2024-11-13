# short solution but less readable
# concepts: lists, reasoning
def s1_short():
    cols = int(input())
    row1 = [int(n) for n in input().split()]
    row2 = [int(n) for n in input().split()]

    tape_required = 0
    for i in range(cols):
        if i == 0:
            tape_required += (3 * row1[i]) + (3 * row2[i]) - (2 * row1[i] * row2[i])
            continue
        if row1[i] == 1:
            tape_required += 3 - 2 * row1[i - 1]
        if row2[i] == 1:
            tape_required += 3 - 2 * row2[i - 1]
            if i % 2 == 0:
                tape_required -= 2 * row1[i]

    print(tape_required)


def s1_long():
    pass


def asymmetric_difference(heights):
    diff = 0
    for i in range(len(heights) // 2):
        diff += abs(heights[i] - heights[len(heights) - i - 1])
    return diff


def min_asymmetric_difference(heights, cropped_size):
    min_found = asymmetric_difference(heights[0:cropped_size])
    for start_mountain in range(1, len(heights) - cropped_size + 1):
        cropped_mountains = heights[start_mountain:start_mountain + cropped_size]
        cur_asymmetric_difference = asymmetric_difference(cropped_mountains)
        min_found = min(min_found, cur_asymmetric_difference)
    return min_found


# Symmetric Mountain Crop
def s2():
    num_mountains = int(input())
    mountain_heights = [int(h) for h in input().split()]

    min_asymmetric_differences = []

    for cropped_size in range(1, num_mountains + 1):
        m = min_asymmetric_difference(mountain_heights, cropped_size)
        min_asymmetric_differences.append(str(m))

    print(" ".join(min_asymmetric_differences))


s2()