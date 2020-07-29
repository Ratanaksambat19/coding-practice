# def arrayChuck(arr, size):
#     container = []
#     if len(arr) > size:
#         for i in range(0, len(arr), size):
#             container.append(arr[i:size+i])
#         return container
#     return arr
# print(arrayChuck([1,2,3,4], 5))


# def arrayChuck(arr, size):
#     for i in range(0, len(arr), size):
#         yield arr[i:size+i]

# x = arrayChuck([1,2,3,4,5], 2)
# print(list(x))


# def arrayChuck(arr, size):
#     return [arr[i:i+size] for i in range(0, len(arr), size)]

# print(arrayChuck([1,2,3,4], 2))


# def arrayChuck(arr, size):
#     chunked_arr = []
#     for elem in arr:
#         chunked_elem = chunked_arr[len(chunked_arr) - 1]
#         if len(chunked_arr) == 0 or len(chunked_arr) == size:
#             chunked_arr.append([elem])
#         else:
#             chunked_elem.append(elem)
#     return chunked_arr
# print(arrayChuck([1,2,3,45,5], 2))

def arrayChuck(arr, size):
    chunked = []
    index = 0
    while index < len(arr):
        chunked.append(arr[index:size + index])
        index += size
    return chunked
print(arrayChuck([1,2,3,4,5], 2))

