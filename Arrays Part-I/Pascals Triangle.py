# Given an integer N, return the first N rows of Pascal’s triangle

def pascalsTriangle(n):
    if n == 2:
        return [1, 1]
    elif n == 1:
        return [1]

    lastRow = pascalsTriangle(n-1)
    newRow = [1 for i in range(len(lastRow) + 1)]
    for i in range(1, len(lastRow)):
        newRow[i] = lastRow[i-1] + lastRow[i]
    return newRow


if __name__ == '__main__':
    n = 6
    for i in range(n):
        values = pascalsTriangle(i+1)
        for j in range(n-1-i):
            print(" ", end='')
        for j in values:
            print(j, end=' ')
        print()
  