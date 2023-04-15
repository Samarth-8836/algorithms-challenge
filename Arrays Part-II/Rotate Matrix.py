# Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

def rotate(matrix):
    n = len(matrix) - 1
    for i in range(n + 1):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n + 1):
        lPointer = 0
        rPointer = n
        while lPointer < rPointer:
            matrix[i][lPointer], matrix[i][rPointer] = matrix[i][rPointer], matrix[i][lPointer]
            lPointer += 1
            rPointer -= 1

    return matrix

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(matrix))