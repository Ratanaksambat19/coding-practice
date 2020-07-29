def fizzbuzz(n):
    string = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            string += "fizzbuzz" + '\n'
        elif i % 3 == 0:
            string += "fizz"+'\n'
        elif i % 5 == 0:
            string += "buzz" + '\n'
        else:
            string += str(i) + '\n'
    return string
print(fizzbuzz(15))