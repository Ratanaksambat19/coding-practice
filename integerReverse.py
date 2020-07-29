# def reverInt(n):
#     sign = -1 if n < 0 else 1
#     check = 0
#     string = ''
#     n = abs(n)
#     while n > 0:
#         check = int(n) % 10
#         string = string + str(check)
#         n = n//10
#     return int(string) * sign
# print(reverInt(-1500))

def reverInt(n):
    n = "".join(list(reversed(str(n))))
    if n[-1] == '-':
        return int(n[:len(n)-1]) * -1
    return int(n)
print(reverInt(159049))