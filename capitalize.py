# def capitalize(string):
#     sp_string = string.split()
#     empty = ''
#     for word in sp_string:
#         word = list(word)
#         if word[0].isalpha():
#             word[0] = word[0].upper()
#             jo_string = "".join(word)
#             empty += jo_string + " "
#         else:
#             check = 0
#             while word[check].isalpha() == False:
#                 check += 1
#                 word[check] = word[check].upper()
#                 if word[check].isalpha():
#                     jo_string = "".join(word)
#                     empty += jo_string + " "
                
#     return empty
# print(capitalize("!443hello world"))

# def capitalize(string):
#     return [word.capitalize() for word in string.split()]
# print(capitalize("!443hello world"))

def capitalize(string):
    word_list = string[0].upper()
    string = list(string)
    for idx in range(1, len(string) - 1):
        if word_list[idx - 1] == " ":
            word_list += string[idx].upper()
        else:
            word_list += string[idx]
    return word_list

print(capitalize("hello world python"))