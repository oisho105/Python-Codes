
def sort(nums):
    length = len(nums)
    for i in range(0,length,1):
        minpos = i
        for j in range(i,length):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]      # the swapping
        nums[i] = nums[minpos]
        nums[minpos] = temp

    return 0

nums = [7,21,23,11,5,2]
sort(nums)
print(nums)
