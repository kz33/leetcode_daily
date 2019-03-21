# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        if l == 0:
            return None
        cnt = 1
        for i in range(l):
            t = digits[l - 1 - i] + cnt
            if t == 10:
                cnt = 1
                digits[l - 1 - i] = 0
                if l - 1 - i == 0:
                    digits.insert(0, 1)
                    return a
            else:
                cnt = 0
                digits[l - 1 - i] =t
        return digits


s = Solution()
digits = [1,2,3]
a = s.plusOne(digits)
print(a)
