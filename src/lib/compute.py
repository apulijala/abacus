class Compute(object):
    
    def __init__(self, operands,operator):
        self.operands = operands
        self.operator = operator
        

    def add(self, a, b):
        pass 

    def subtract(self, a, b):
        pass 

    def multiply(self):
        product = 1
        for item in self.operands:
            product *= item 
        print(product)


    
    def divide(self, a, b):
        quotient = 1
        for item in self.operands:
            quotient /= item 
        print(quotient)
    