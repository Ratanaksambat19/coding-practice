# def finbonnacci(num):
#     container = [0, 1]
#     for i in range(1, num):
#         check = container[i] + container[i - 1]
#         container.append(check)
#     return container[num - 1]
  
# print(finbonnacci(10))

##USSING recursion
# def finbonnacci(num):
#     if num < 2:
#         return num
#     return finbonnacci(num - 1) + finbonnacci(num - 2)

# print(finbonnacci(9))


##With memorization
def memoize(fn):
    container = {}
    def helper(n):
        if n not in container:
            container[n] = fn(n)
        return container[n]
    return helper
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci = memoize(fibonacci)

print(fibonacci(50))

