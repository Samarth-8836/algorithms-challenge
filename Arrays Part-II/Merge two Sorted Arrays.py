# Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

def mergeSortArrays(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    i1 = i2 = 0
    if l1 > 0 and l2 == 0:
        return [arr1, arr2]
    if l1 == 0 and l2 > 0:
        return [arr2, arr1]
    if arr1[i1] < arr2[i2]:
        pass
    else:
        arr1[i1], arr2[i2] = arr2[i2], arr1[i1]
    i1 += 1
    swapNumber = passNumber = 0
    while swapNumber + passNumber < l1 - 1:
        # print(f"{i1} {i2} {arr1} {arr2} {swapNumber} {passNumber}")
        if arr1[i1] > arr2[i2]:
            arr1[i1], arr2[i2] = arr2[i2], arr1[i1]
            i1 += 1
            x = i2 + 1
            flag = False
            while x < l2 and arr2[i2] > arr2[x]:
                x += 1
                flag = True
            if flag:
                arr2.insert(x, arr2[i2])
                del arr2[i2]
            swapNumber += 1
        elif arr1[i1] == arr2[i2]:
            i1 += 1
            passNumber += 1
        else:
            i2 += 1 
            passNumber += 1

    # for i in arr2:
    #     arr1.append(i)
    return [arr1, arr2]

if __name__ == '__main__':
    arr1 = [10] 
    arr2= [1]
    print(mergeSortArrays(arr1, arr2))