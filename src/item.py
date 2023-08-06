class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity_of_goods) -> None:
        self.name = name
        self.price = price
        self.quantity_of_goods = quantity_of_goods
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity_of_goods

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

