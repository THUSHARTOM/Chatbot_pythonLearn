# Define your exception up here:
class OutOfStock(Exception):
    """Exception"""


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock
        print(self.stock.keys())

    def buy(self, color):
        if self.stock[color] == 0:
            print("hi")
            raise OutOfStock

        else:
            self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')