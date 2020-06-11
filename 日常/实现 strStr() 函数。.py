# -*- coding: utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" :
            return 0
        n_size = len(needle)
        h_size = len(haystack)
        for i in range(h_size-n_size+1):
            if haystack[i:i+n_size] == needle:
                return i
        return -1
    
        # solution 1 :
        # haystack.find(needle)
        
        

s = Solution()
haystack = "hello"
needle = "ll"
a = s.strStr(haystack,needle)
print(a)
