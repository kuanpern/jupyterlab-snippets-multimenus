class BPSomeClass(object):
    """Brief class description
    
    Some more extensive description
    
    Attributes
    ----------
    attr1 : string
        Purpose of attr1.
    attr2 : float
        Purpose of attr2.
    
    """
    
    def __init__(self, param1, param2, param3=0):
        """Example of docstring on the __init__ method.
        
        Parameters
        ----------
        param1 : str
            Description of `param1`.
        param2 : float
            Description of `param2`.
        param3 : int, optional
            Description of `param3`, defaults to 0.
        
        """
        self.attr1 = param1
        self.attr2 = param2
        print(param3 // 4)
    
    @property
    def attribute2(self):
        return self.attr2
    
    @attribute2.setter
    def attribute2(self, new_attr2):
        if not isinstance(float, new_attr2):
            raise ValueError("attribute2 must be a float, not {0}".format(new_attr2))
        self.attr2 = new_attr2


bp_obj = BPSomeClass("a", 1.618)
print(bp_obj.attribute2)
bp_obj.attribute2 = 3.236
