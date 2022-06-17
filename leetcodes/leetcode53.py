def maxSubArray():
    nums = [-1,-1]
    maxsum = nums[0]
    sumnum = 0


    for i in nums:
        if sumnum < 0:
            sumnum = 0
        sumnum += i
        maxsum = max(maxsum,sumnum)

    return maxsum


print(maxSubArray())




