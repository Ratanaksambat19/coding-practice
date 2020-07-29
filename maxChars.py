# def maxChar(word):
#     map = {}
#     for i in word:
#         map[word.count(i)] = i
#     check = sorted(map.keys())[-1]
#     print(map)
#     return map[check]
# print(maxChar("He111111111111ooo hiiii ee"))

from collections import Counter
def maxChar(word):
    max_num = 0
    max_char = ''
    map = Counter(word)
    for item in map:
        if (map[item] > max_num):
            max_num = map[item]
            max_char = item
    return max_char
print(maxChar("H1ooo hiiii ee"))

# def maxChar(word):
#     map = {}
#     max_num = 0
#     max_char = ''
#     for i in word:
#         map[i] = 0
#     for i in word:
#         if map[i]:
#             map[i] += 1
#         else:
#             map[i] = 1
#     for item in map:
#         if (map[item] > max_num):
#             max_num = map[item]
#             max_char = item
#     return max_char
# print(maxChar("H1ooo hiiii ee"))