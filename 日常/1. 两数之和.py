# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None:
            return []
        size = len(nums)
        res = []
        ok = False
        for i in range(size):
            if not ok:
                first = target - nums[i]
                if first in nums[(i+1):]:
                    ok = True
                    res.append(i)
                else:
                    continue

            else:
                second = target - nums[res[0]]
                if nums[i] == second:
                    res.append(i)
                    break
        return res


class Solution_standard:
    def twoSum(self, nums, target):
        res_map = {}
        for index,num in enumerate(nums):
            a = target - num
            if a in res_map:
                return [res_map[a],index]
            res_map[num] = index
        return None


s = Solution_standard()
nums = [2,7,11,15]
target = 9
res = s.twoSum(nums,target)
print(res)