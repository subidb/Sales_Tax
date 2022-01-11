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