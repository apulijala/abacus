class Compute(object):
    
    def __init__(self, operands,operator):
        self.operands = operands
        self.operator = operator

    def add(self, a, b):
        sum = 0
        for item in self.operands:
            sum += item 
        print(sum) 

    # Enabling subtraction here. 

    def subtract(self, a, b):
        difference = 0
        for item in self.operands:
            difference -= item 
        print(difference)

    # Enabling Multiplicaton here. 
    def multiply(self):
        product = 1
        for item in self.operands:
            product *= item 
        print(product)
    
    def divide(self, a, b):
        return a/b
    
    def mytest(self, a, b):
        return "test"
