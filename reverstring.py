# def revers(word):
    # return word[::-1]

# def revers(word):
    # string = ""
    # for i in range(len(word) - 1, -1, -1):
    #     print(i)
    #     string += word[i]
    # return string

# def revers(word):
#     string = ""
#     for i in word:
#         string = i + string
#     return string

import functools
def revers(word):
    return functools.reduce(lambda a, b: b + a, word)

print(revers("apple"))
print(revers("!hello"))
print(revers("Greeting!"))