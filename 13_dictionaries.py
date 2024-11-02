# Motivating example: class of students with marks
# - could use individual variables but not really nice
# - could use a list, but then you need to remember an index for each student
# How we would do it with a dictionary:
student_marks = {
    "Clark K": 90,
    "Bruce W": 87,
    "Tony S": 56,
    "Peter P": 76,
    "Diana P": 89,
    "Steve R": 87
}

# Define terms: KEY and VALUE
# Note: in many other languages this is referred to as a MAP
# clark_k_mark = student_marks["Clark K"]
# print("Clark K's mark is:", clark_k_mark)

# Example 2: an actual dictionary (explains why it's called a dictionary)
# my_dictionary = {
#     "serendipity": "the occurrence of events by chance in a happy or beneficial way",
#     "ephemeral": "lasting for a very short time",
#     "ubiquitous": "present, appearing, or found everywhere",
#     "nebulous": "in the form of a cloud or haze; unclear or vague",
#     "quixotic": "exceedingly idealistic; unrealistic and impractical",
#     "ineffable": "too great or extreme to be expressed in words",
#     "insidious": "proceeding in a gradual, subtle way, but with harmful effects",
#     "magnanimous": "generous or forgiving, especially toward a rival or less powerful person",
#     "esoteric": "intended for or likely to be understood by only a small number of people",
#     "taciturn": "reserved or uncommunicative in speech; saying little"
# }

# # "Lookup" a word, just like you would do in a dictionary
# print(my_dictionary["ephemeral"])


# Example 3: Song info (artist, album, genre, length)
# let_it_go = {
#     "title": "Let It Go",
#     "artist": "Idina Menzel",
#     "album": "Frozen (Original Motion Picture Soundtrack)",
#     "release_year": 2013,
#     "genre": ["Pop", "Soundtrack"],
#     "duration_seconds": 219
# }

# print(let_it_go["artist"])

# empty_dictionary = {}

# You CAN'T have duplicate keys:
# student_marks = {
#     "Floyd M": 98,
#     "Floyd M": 77
# }
# print(student_marks["Floyd M"])  # What would this be? Let's see
# print(student_marks)  # Notice what happened, one of them simply got replaced

# You CAN have duplicate values:
# student_marks = {
#     "Ryan G": 82,
#     "Gervonta D": 82
# }
# print(student_marks)

# Exercise: create example dictionaries for the following:
#  - your favourite song from a few different artists
#  - your favourite player from a few different sports
#  - language-to-language dictionary (ex. English-French)
#  - report card with marks for a single student for a few different subjects


# Dict operations
student_marks = {
    "Clark K": 90,
    "Bruce W": 87,
    "Tony S": 56,
    "Peter P": 76,
    "Diana P": 89,
    "Steve R": 87
}
print(student_marks)
print(len(student_marks))
print(student_marks["Clark K"])
# print(student_marks["James B"])  # KeyError
print(student_marks.get("Clark K"))
print(student_marks.get("James B"))  # None
print(student_marks.get("James B", 0))  # Default value: 0
