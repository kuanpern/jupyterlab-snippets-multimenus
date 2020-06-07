class BPSomeClass(object):
    r"""Describe the class"""
    def __init__(self, arg1, arg2):
        self.attr1 = arg1
        self.attr2 = arg2
    
    def attribute1(self):
        return self.attr1
bp_obj = BPSomeClass("a", 2.7182)
bp_obj.attribute1()