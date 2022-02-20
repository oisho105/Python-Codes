
def sort(nums):
    length = len(nums)-1
    for i in range(length,0,-1):
        for j in range(i):     # after ech loop, the highest value goes last
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return 0

nums = [7, 1, 501, 77, 33, 241, 110]
sort(nums)         # defining a list
print(nums)
