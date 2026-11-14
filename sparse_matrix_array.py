matrix = [[0, 0, 3, 0], [0, 0, 5, 7], [0, 0, 0, 0], [0, 2, 6, 0]]

rows = len(matrix)
cols = len(matrix[0])
sparse = []

# Header: [total_rows, total_cols, non_zero_count]
non_zero = sum(1 for r in matrix for val in r if val != 0)
sparse.append([rows, cols, non_zero])
# iterate on the rows and columns
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            sparse.append([i, j, matrix[i][j]])

print("Row\tCol\tValue")
for row in sparse:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")
