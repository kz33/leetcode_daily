# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
#
# 示例 1:
#
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
# 示例 2:
#
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
# 说明:
#
# 数组的长度不会超过10,000。
# 你可以认为所有数字总和在 32 位有符号整数范围内。

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = len(nums)
        _sum = 0

        if s < 2:
            return False
        for i in range(s - 1):
            _sum +=i
            if nums[i] == 0 and nums[i + 1] == 0 and k == 0:
                return True

        if k == 0:
            return False
        for i in range(s - 1):
            sum0 = nums[i] + nums[i + 1]
            print(nums[i] ,nums[i + 1])
            print(sum0)
            print(sum0 / k)
            print(sum0 % k)
            print("========")
            if sum0 % k == 0:
                return True
        if _sum % k == 0:
            return True
        return False


s = Solution()

nums = [470,161,377,184,118,91,413,73,224,167,505,413,521,5,7,372,393,523,211,479,90,516,238,467,410,51,337,31,442,297,100,75,260,33,490,477,21,374,233,41,215,87,84,153,271,241,169,275,323,358,291,176,423,426,296,175,413,423,387,416,27,266,257,136,27,155,77,142,60,335,401,443,52,153,345,71,117,443,177,238,433,464,323,79,156,429,79,327,64,335,92,147,350,480,277,335,97,317,420,453]
k=75
print(nums)
a = s.checkSubarraySum(nums,k)
print(a)