# Given an integer N, return the first N rows of Pascal’s triangle

def pascalsTriangle(storage):
    if not len(storage):
        storage.append([1])
        return storage
    
    lastRow = storage[-1]
    newRow = [1 for i in range(len(lastRow) + 1)]
    for i in range(1, len(lastRow)):
        newRow[i] = lastRow[i-1] + lastRow[i]
    
    storage.append(newRow)
    return storage


if __name__ == '__main__':
    n = 6
    storage = []
    for i in range(n):
        storage = pascalsTriangle(storage)
        for j in range(n-1-i):
            print(" ", end='')
        for j in storage[-1]:
            print(j, end=' ')
        print()
  