# Given an array nums with n objects numbered 0, 1, or 2, sort them in-place.

def sortColors(nums):
    i = 0
    compares = 0
    while compares < len(nums):
        compares += 1
        if nums[i] == 0:
            del nums[i]
            nums.insert(0, 0)
            i += 1
        elif nums[i] == 2:
            del nums[i]
            nums.insert(len(nums), 2)
        else:
            i += 1
    return nums


if __name__ == '__main__':
    print(sortColors([2,0,2,1,1,0]))