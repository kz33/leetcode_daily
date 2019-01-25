# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min is None:
            self.min = x
        if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        peak = self.stack.pop()
        if self.min == peak:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

