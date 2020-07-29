# def palindrome(string):
#     string = str(string)
#     return string == string[::-1]
# print(palindrome(12321))

# import functools
# def palindrome(string):
#     rev = functools.reduce(lambda a, b: b + a, str(string))
#     return rev == str(string)
# print(palindrome(12321))

# def palindrome(string):
#     word = ""
#     for i in str(string):
#         word = i + word
#     return str(string) == word
# print(palindrome(12321))

