from Point import Point

def read_table(path):
    table = []
    with open(path, "r") as file:
        for line in file:
            row = list(map(float, line.split(" ")))
            table.append(row)

    return sorted(table, key=lambda x: x[0])

def print_table(pointTable):
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")
    print("| {:^5s} | {:^10s} | {:^10s} |".format("№", "X", "Y", "Y\'"))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")
    for i in range(len(pointTable)):
        print("| {:^5d} | {:^10.3f} | {:^10.3f} |".format(i, pointTable[i][0], pointTable[i][1]))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")

def get_nearest_in_mat(mat, n, x):
    if len(mat) < n:
        raise ValueError("Not enough matrix size")
    # diff = x - mat[0][0]
    i = 1
    while i < len(mat) and x - mat[i][0] > 0:
        # diff = mat[i][0] - x
        i += 1
    if i == len(mat):
        return mat[-n:]
    # print(i)
    res = []
    j = i - 1
    while len(res) < n:
        if (i >= len(mat) and j < 0):
            raise ValueError("Not enough matrix size")
        if (j >= 0):
            res.append(mat[j])
            j -= 1
        if (i < len(mat) and len(res) < n):
            res.append(mat[i])
            i += 1
    return sorted(res, key=lambda x: x[0])            
