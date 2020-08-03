# def pyramid(num):
#     pyra = ''
#     space = 1
#     for row in range(1, num + 1):
#         k = 0
#         while space <= num - row:
#             pyra += ' '
#             space += 1

#         while k != 2*row - 1:
#             pyra += '*'
#             k += 1
#         print(pyra)
# print(pyramid(3))

# import math
# def pyramid(num):
#     midpoint = math.floor((2*num - 1)/2)
#     for row in range(num):
#         stair = ''
#         for col in range(num * 2 - 1):
#             if (midpoint - row) <= col and (midpoint + row) >= col:
#                 stair += '#'
#             else:
#                 stair += ' '
#         print(stair)

# print(pyramid(3))
import sys
sys.setrecursionlimit(10**6) 
import math
def pyramid(num, row = 0, level = ''):
    if row == num :
        return 
    
    if len(level) == 2 * num - 1:
        print(level)
        return pyramid(num, row+1)

    midpoint = math.floor((2*num - 1)/2)
    addlev = ''
    if (midpoint - row <= len(level)) and (midpoint + row >= len(level)):
        addlev += "#"
    else:
        addlev += " "
    
    return pyramid(num, row, level + addlev)

print(pyramid(5))




