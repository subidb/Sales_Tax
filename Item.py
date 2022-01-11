import math

class Item: #Item class with all the attributes
    def __init__(self, name, quantity, price, tax=0, price_after_tax=0, excempt=False, imported=False):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.tax = tax
        self.excempt = excempt
        self.imported = imported
        self.price_after_tax = price_after_tax
        
    def __repr__(self):
        return "\n[name:{}, quantity:{}, price:{}, excempt:{}, imported:{}, tax:{:.2f}, price_after_tax:{:.2f}]"\
            .format(self.name, self.quantity, self.price, self.excempt, self.imported, self.tax, self.price_after_tax) 
            
            
    def sales_tax(self): #sets sales tax percentage on the item based on the given information
        
        if self.excempt == False and self.imported == False:
            self.tax_rate = 0.1 
            
        if self.excempt == False and self.imported == True:
            self.tax_rate = 0.15
            
        if self.excempt == True and self.imported == False:
            self.tax_rate = 0
            
        if self.excempt == True and self.imported == True:
            self.tax_rate = 0.05 
            
            
    def tax_calc(self): #calculates the tax on the good based on the information 
        self.tax = self.tax_rate * self.price
        self.tax = math.ceil(self.tax / 0.05) * .05
        self.price_after_tax  = self.price + self.tax