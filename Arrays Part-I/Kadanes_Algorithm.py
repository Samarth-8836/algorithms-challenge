# Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and returns its sum and prints the subarray.

def maxSubArray(nums):
    largestSumArray = [0, -1, len(nums)]
    potentialLargestSumArray = [0, -1, len(nums)]
    currentSum = 0
    for i in range(len(nums)):
        if nums[i] + currentSum < 0:
            currentSum = 0
            potentialLargestSumArray = [0 , -1, len(nums)]
        else:
            currentSum += nums[i]
            if potentialLargestSumArray[1] == -1:
                potentialLargestSumArray = [currentSum, i, i]
            else:
                potentialLargestSumArray = [currentSum, potentialLargestSumArray[1], i]

        if potentialLargestSumArray[0] > largestSumArray[0]:
            for j in range(3):
                largestSumArray[j] = potentialLargestSumArray[j]
        elif potentialLargestSumArray[0] == largestSumArray[0] and potentialLargestSumArray[1] + potentialLargestSumArray[2] < largestSumArray[1] + largestSumArray[2]:
            for j in range(3):
                largestSumArray[j] = potentialLargestSumArray[j]
            
    return largestSumArray


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))