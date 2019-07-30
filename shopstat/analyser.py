import loader


def calculate_receipt_price(receipt):
    df = receipt.get_products()
    total_prices = df['Price'] * df['Amount']
    return total_prices.sum()


def test():
    receipt = loader.test()
    print(calculate_receipt_price(receipt))
