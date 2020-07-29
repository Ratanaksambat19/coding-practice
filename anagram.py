# import re
# def anagram(string1, string2):
#     string1 = string1.lower()
#     string2 = string2.lower()
#     check1 = re.findall(r"[a-z]", string1)    
#     check2 = re.findall(r"[a-z]", string2)

#     return sorted(check1) == sorted(check2)

# print(anagram("rail !safety!", "fairy tales   "))


#check string
# import re
# def check(string):
#     map = {}
#     check = re.sub(r'[^A-Za-z]', '', string).lower()
#     for i in check:
#         map[i] = 0
#     for char in check:
#         map[char] += 1
#     return map

# def anagram(string1, string2):
#     check1 = check(string1)
#     check2 = check(string2)
#     if len(check1) != len(check2):
#         return False
#     for i in check1.keys():
#         try:
#             if check1[i] != check2[i]:
#                 return False
#         except:
#             return False
#     return True

# print(anagram("wXxglscZ", "xlcspblg"))

import re
def cleanString(string):
    return sorted(list(re.sub(r'[^a-zA-Z]', "", string).lower()))

def anagram(string1, string2):
    return cleanString(string1) == cleanString(string2)

print(anagram("wXxglscZ", "xlcspblg"))
print(anagram("rail !safety!", "fairy tales   "))