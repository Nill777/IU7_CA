import numpy as np

def newton_solve1(matrix_fn, func, start_approx, eps=1e-5):
    n_vars = len(start_approx)
    coefs = matrix_fn(*start_approx)
    fn_values = -func(*start_approx)
    # print(coefs, "\n--------\n", fn_values)
    deltas = np.linalg.solve(coefs, fn_values).reshape((n_vars,))
    # print(coefs, "\n--------\n", fn_values)

    approx = start_approx + deltas

    while any(map(lambda x: abs(x) >= eps, deltas / approx)):
        coefs = matrix_fn(*approx)
        fn_values = -func(*approx)

        deltas = np.linalg.solve(coefs, fn_values).reshape((n_vars,))
        # print(coefs, "\n--------\n", fn_values)
        approx += deltas
    # print("approx", approx)
    return approx
import numpy as np

def newton_solve(matrix_fn, func, start_approx, eps=1e-5):
    n_vars = len(start_approx)
    coefs = matrix_fn(*start_approx)
    fn_values = -func(*start_approx)

    deltas = run(coefs, fn_values)

    approx = start_approx + deltas

    while any(map(lambda x: abs(x) >= eps, deltas / approx)):
        coefs = matrix_fn(*approx)
        fn_values = -func(*approx)

        deltas = run(coefs, fn_values)

        approx += deltas

    return approx

def run(matrix, F):
    B = np.diagonal(matrix).copy() 
    A = np.diagonal(matrix, offset=-1)
    C = np.diagonal(matrix, offset=1) 
    n = len(B)
    for i in range(1, n):
        temp = A[i - 1] / B[i - 1]
        B[i] = B[i] - temp * C[i - 1]
        F[i] = F[i] - temp * F[i - 1]
    res = np.zeros(n)
    res[-1] = F[-1] / B[-1]
    for i in range(n - 2, -1, -1):
        res[i] = (F[i] - C[i] * res[i + 1]) / B[i]

    return res

# def tridiagonal_solve(matrix, rhs):
#     n = matrix.shape[0]
#     a = np.zeros(n)
#     b = np.zeros(n)
#     c = np.zeros(n)
#     d = np.zeros(n)

#     a[0] = 0
#     b[0] = 1
#     c[0] = 0
#     d[0] = rhs[0]

#     for i in range(1, n):
#         a[i] = matrix[i, i-1]
#         b[i] = matrix[i, i]
#         c[i] = matrix[i, i+1] if i < n-1 else 0
#         d[i] = rhs[i]

#     x = np.zeros(n)

#     for i in range(1, n):
#         m = a[i] / b[i-1]
#         b[i] -= m * c[i-1]
#         d[i] -= m * d[i-1]

#     x[n-1] = d[n-1] / b[n-1]

#     for i in range(n-2, -1, -1):
#         x[i] = (d[i] - c[i] * x[i+1]) / b[i]

#     return x