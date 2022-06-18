def merge():
    nums1 = [4,5,6,0,0,0]
    m = 3
    q = m
    nums2 = [1,2,3]
    n = 3
    i = 0


    while nums2:
        nums1[q] = nums2.pop(0)
        m = q
        print(nums2)
        while nums1[m] < nums1[m-1] and m > 0:
            nums1[m], nums1[m-1] = nums1[m-1], nums1[m]
            m -= 1
        q += 1

    print(nums1)


merge()