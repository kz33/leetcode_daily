# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
# 注意:
# n 是正数且在32为整形范围内 ( n < 231)。
# 示例 1:
# 输入:
# 3
# 输出:
# 3

# 示例 2:
# 输入:
# 11
# 输出:
# 0
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        _len = 1
        base = 9 
        start = 1
        while n > base * _len:
            n = n - base * _len
            base = base * 10
            _len +=1
            start *= 10
        start += (n-1)/_len
        return int(str(start)[(n-1)%_len])
s = Solution()
n = 23456
a = s.findNthDigit(n)
