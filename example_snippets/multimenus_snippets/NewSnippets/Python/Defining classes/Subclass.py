class BP_A(object):
    def __init__(self, param1):
        self.attr1 = param1

class BP_B(BP_A):
    def __init__(self, param1, param2):
        super(BP_B, self).__init__(param1)
        self.attr2 = param2


bp_b = BP_B("a", "b")
print(bp_b.attr1, bp_b.attr2)