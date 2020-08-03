# def step(n):
#     string = ''
#     for _ in range(n):
#         string += '#'
#         print(string)
# print(step(5))

# def step(n):
#     string = ''
#     i = 0
#     while i < n:
#         string += '#'
#         i += 1
#         print(string)
# print(step(5))

# def step(n):
#     i = 1
#     while i <= n:
#         print("#" * i)
#         i += 1
# print(step(5))

# def step(n):

#     for row in range(n):
#         string = ''
#         for col in range(n):
#             if col <= row:
#                 string += '#'
#             else:
#                 string += ' '
#         print(string)

# print(step(5))

# def step(n):
#     if n == 0:
#         return 
#     print(n * '#')
#     return step(n - 1)

# print(step(5))

import sys
sys.setrecursionlimit(10**6) 

def step(n, row = 0, stair = ''):

    if n == row:
        return None
    
    if n == len(stair):
        print(stair)
        step(n, row + 1)

    if len(stair) <= row:
        stair += '#'
        # print(stair)
    else:
        stair += ' '

    step(n, row, stair)

print(step(5))