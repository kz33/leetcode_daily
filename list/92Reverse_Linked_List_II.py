# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new = None
        print(id(head))
        cur = head
        count = 1
        while cur and count < m:
            new = cur
            cur = cur.next
            count += 1
        pre = new
        t2 = cur

        while cur and count <= n:
            tmp = cur.next
            cur.next = new
            new = cur
            cur = tmp
            count +=1

        pre.next = new
        t2.next = cur
        print(id(head))
        return  head

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
m = 2
n = 4
a = s.reverseBetween(head, m, n)
print(
    a.val,
    a.next.val,
    a.next.next.val,
    a.next.next.next.val,
    a.next.next.next.next.val)
