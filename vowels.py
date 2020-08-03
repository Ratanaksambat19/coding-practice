# def vowels(phrase):
#     count = 0
#     for char in phrase:
#         if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
#             count += 1
#     return count
# print(vowels("Hi there, why do you ask ?"))

# def vowels(phrase):
#     map_vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#     for char in phrase:
#         if char in map_vowel.keys():
#             map_vowel[char] += 1
#     return sum(list(map_vowel.values()))

# print(vowels("Hi there, why do you ask ?"))

import re
def vowels(phrase):
    match = re.findall(r'[aeiou]', phrase)
    return len(match)

print(vowels("Hi there, why do you ask iiii?"))

