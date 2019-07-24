import pandas as pd

class Receipt:
    '''
    Represents receipt as an object.
    '''
    def __init__(self, date):
        self.date = date
        self.products = pd.DataFrame(columns=['Name', 'Type', 'Price', 'Amount'])
    
    def add_product(self, product, amount):
        row = product.get_attributes()
        row['Amount'] = amount
        self.products = self.products.append(row, ignore_index=True)
    
    def get_products(self):
        return self.products


class Product:
    '''
    Represents product.
    '''
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
    
    def get_attributes(self):
        return {'Name': self.name, 'Type': self.type, 'Price': self.price}


def test():
    p1 = Product('milk', 'diary', 2.99)
    p2 = Product('organges', 'fruits', 1.05)
    receipt = Receipt()
    print(receipt.get_products())
    receipt.add_product(p1, 2)
    print(receipt.get_products())
    receipt.add_product(p2, 0.5)
    print(receipt.get_products())
    return receipt