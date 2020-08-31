n = int(input())
lst = [ int(x) for x in input().split() ]
j = 1
count = 0
sum = 0

for i in range(0, n - 1):
    
    while (n > j and count != n):
        mul = lst[j] * lst[i]
        sum += mul
        j += 1
        count += 1
        print(lst[i], lst[j - 1])
    j = n - 1
    
print(sum)

    
    