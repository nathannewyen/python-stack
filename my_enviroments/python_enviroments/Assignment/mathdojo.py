class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        self.result = self.result + sum(nums)
        return self

    def subtract(self, *nums):
        self.result = self.result - sum(nums)
        return self


# create an instance:
md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).subtract(2, 2).result
print(x)  # should print 5
