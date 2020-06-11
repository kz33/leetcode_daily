# -*- coding: utf-8 -*-
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 
# 所有输入只包含小写字母 a-z 。

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in zip(*strs):
            print(i)
        same = ''
        for item in strs:
            if item =='':
                return ""
            if same == "":
                same = item
            else:
                l = min(len(same),len(item))
                i=0
                new_same = ''
                while l>0:
                    if same[i]==item[i]:
                        new_same += same[i]
                    elif not new_same:
                        break
                    i+=1
                    l-=1
                if not new_same:
                    return ''
                same = new_same
        return same
        
        # solution 1:
        # if strs == [] or strs == None:
        #     return ""
        # 
        # s1 = min(strs)
        # s2 = max(strs)
        # print(s1, s2)
        # 
        # for i, x in enumerate(s1):
        #     if x != s2[i]:
        #         return s2[:i]
        # return s1
        
        # solution 2 :
        # res = ''
        # for tmp in zip(*words):
        #     tmp_set = set(tmp)
        #     if len(tmp_set) == 1:
        #         res += tmp[0]
        #     else:
        #         break
        # return (res)

s = Solution()
strs = ["afla","bflaw","cflight",'dflower']
a = s.longestCommonPrefix(strs)
print(a)