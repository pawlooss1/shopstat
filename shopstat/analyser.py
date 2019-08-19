import loader
import numpy as np


def calculate_receipt_price(receipt):
    df = receipt.get_products()
    total_prices = df['Price'] * df['Amount']
    rounded_prices = round_prices(total_prices.astype('float64'))
    return rounded_prices.sum()


def round_prices(prices):
    return np.ceil(prices.multiply(100)).divide(100)


def test():
    receipt = loader.test()
    print(calculate_receipt_price(receipt))
