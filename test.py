# -*- coding: utf-8 -*-
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        for i in range(size):
            if not s.__contains__(s[i]):
                return i

s = Solution()
x = "leetcode"
a = s.firstUniqChar(x)
print(a)