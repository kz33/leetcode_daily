# -*- coding: utf-8 -*-


lst = [7,4,2,6]


k = 6


def judge(nums,k):
    size = len(nums)
    if size<2:
        return False

    for i in range(size):
        if nums[i]<=k:
            tmp = nums[i]
            for j in range(1,size-i):
                tmp +=nums[i+j]
                if tmp ==k:
                    return True
                if tmp >k:
                    break
    return False


print(judge(lst,k))