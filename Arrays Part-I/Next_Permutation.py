# Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

def find_just_bigger(element, input_arr):
    '''finds the just bigger element than given element'''
    smallest = input_arr[0]
    index = 0
    for i in range(len(input_arr)):
        if input_arr[i] > element and input_arr[i] < smallest:
            if input_arr[i] < smallest:
                smallest = input_arr[i]
                index = i

    return [smallest, index]

def partial_sort(index, input_arr):
    '''sorts an array from given index to end in ascending order'''
    temp_arr = [input_arr[i] for i in range(index, len(input_arr))]
    temp_arr.sort()
    j = 0
    for i in range(index, len(input_arr)):
        input_arr[i] = temp_arr[j]
        j += 1
    return input_arr


def next_permutation(input_arr):
    '''Bubble sort from the right end to change position of first decending ordered numbers'''
    for i in range(len(input_arr) - 2, -1, -1):
        if input_arr[i] < input_arr[i+1]:
            [element, relative_index] = find_just_bigger(input_arr[i], input_arr[i+1:])
            absolute_index = relative_index + i + 1
            input_arr[absolute_index], input_arr[i] = input_arr[i], input_arr[absolute_index]
            partial_sort(i+1, input_arr)
            return input_arr
    return sorted(input_arr)

if __name__ == '__main__':
    arr = [1,3,2]
    print(next_permutation(arr))
