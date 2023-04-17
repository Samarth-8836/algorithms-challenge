# Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.
def firstElement(a):
    return a[0]

def merge(intervals):
    if len(intervals) == 1:
        return intervals
        
    intervals.sort(key=firstElement)
    
    i = 1
    while True:
        if i >= len(intervals):
            break
        newOne = [0,0]
        if intervals[i][0] <= intervals[i-1][1]:
            if intervals[i][1] >= intervals[i-1][1]:
                newOne = [intervals[i-1][0], intervals[i][1]]
            else:
                newOne = [intervals[i-1][0], intervals[i-1][1]]
            del intervals[i]
            del intervals[i-1]
            intervals.insert(i-1, newOne)
        else:
            i += 1
    return intervals


if __name__ == '__main__':
    intervals = [[15,18],[1,3],[2,6],[8,10]]
    print(merge(intervals))