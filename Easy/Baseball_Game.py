class Solution(object):
    def calPoints(self, operations):
        ops = []
        for op in operations:
            if op == "+":
                ops.append(ops[-1] + ops[-2])
            elif op == "D":
                ops.append(ops[-1] * 2)
            elif op == "C":
                ops.pop()
            else:
                ops.append(int(op))
        return sum(ops)
obj = Solution()
print(obj.calPoints(["5","2","C","D","+"]))