def matrixSpiral(num):
    size = [[0, 0, 0] for i in range(num)]
    size[0].append(1)
    print(size[0][0])
    print(size)
    counter = 0

    start_col = 0
    end_col = num - 1

    start_row = 0
    end_row = num - 1

    while start_col <= end_col and start_row <= end_row:
        for start_col in range(end_col):
            size[start_row][start_col] = counter
            counter += 1

        start_row += 1

        for start_row in range(end_row):
            size[start_row][end_col] = counter
            counter += 1

        end_col -= 1

        for start_col in range(0, end_col, -1):
            size[end_row][start_col] = counter
            counter += 1

        end_row -= 1

        for start_row in range(0, end_row, -1):
            size[start_row][start_col] = counter
            counter += 1

        start_col += 1
        
    return size


print(matrixSpiral(3))
