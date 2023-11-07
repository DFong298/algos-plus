import numpy as np

def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    M = np.array([[0]*p for _ in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                M[i][j] += A[i][k]*B[k][j]
    return M

def split(matrix):
    n = len(matrix)
    return (matrix[:n//2, :n//2], 
            matrix[:n//2, n//2:], 
            matrix[n//2:, :n//2], 
            matrix[n//2:, n//2:])

def strassen(A, B):
    if len(A) <= 2:
        return brute_force(A, B)
    
    a, b, c, d = split(A)
    e, f, g, h = split(B)

    p_1 = strassen(a+d, e+h)
    p_2 = strassen(d, g-e)
    p_3 = strassen(a+b, h)
    p_4 = strassen(b-d, g+h)
    p_5 = strassen(a, f-h)
    p_6 = strassen(c+d, e)
    p_7 = strassen(a-c, e+f)

    M_11 = p_1 + p_2 - p_3 + p_4
    M_12 = p_5 + p_3
    M_21 = p_6 + p_2
    M_22 = p_5 + p_1 - p_6 - p_7
    M = np.vstack((np.hstack((M_11, M_12)), np.hstack((M_21, M_22))))
    return M


# n = 2 example
A2 = np.array([
    [2, 3], 
    [9, 1]
])

B2 = np.array([
    [4, 6],
    [7, 7]
])

# n = 4 example
A4 = np.array([
            [2, 3, 9, 1],
            [4, 6, 8, 1],
            [7, 7, 2, 4],
            [2, 8, 1, 3]
        ])

B4 = matrix_b = np.array([
            [6, 3, 7, 5],
            [1, 2, 9, 4],
            [2, 5, 9, 8],
            [3, 7, 6, 9]
        ])

# n = 8 example
A8 = np.array([
            [3, 5, 1, 3, 6, 3, 7, 5],
            [1, 2, 3, 4, 1, 2, 9, 4],
            [4, 5, 6, 8, 2, 5, 9, 8],
            [7, 8, 9, 3, 3, 7, 6, 9],
            [4, 1, 2, 3, 2, 3, 9, 1],
            [1, 2, 1, 6, 4, 6, 8, 1],
            [2, 4, 6, 2, 7, 7, 2, 4],
            [6, 2, 5, 4, 2, 8, 1, 3],
        ])

B8 = matrix_b = np.array([
            [4, 1, 2, 3, 2, 3, 9, 1],
            [1, 2, 1, 6, 4, 6, 8, 1],
            [2, 4, 6, 2, 7, 7, 2, 4],
            [6, 2, 5, 4, 2, 8, 1, 3],
            [3, 5, 1, 3, 6, 3, 7, 5],
            [1, 2, 3, 4, 1, 2, 9, 4],
            [4, 5, 6, 8, 2, 5, 9, 8],
            [7, 8, 9, 3, 3, 7, 6, 9]
        ])

print('Strassen for 2x2 matrix')
print(strassen(A2, B2), '\n')
print('Strassen for 4x4 matrix:')
print(strassen(A4, B4), '\n')
print('Strassen for 8x8 matrix:')
print(strassen(A8, B8), '\n')