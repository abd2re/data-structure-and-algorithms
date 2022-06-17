def searchInsert():
    nums = [1,3,5,6]
    target = 7

    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    return len(nums)


print(searchInsert())