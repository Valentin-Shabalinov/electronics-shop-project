import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
        )

    def __str__(self) -> str:
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open(
            "/Users/a1/SkyPro/electronics-shop-project/src/items.csv", newline=""
        ) as csfile:
            reader = csv.DictReader(csfile)
            for row in reader:
                print(row["name"], row["price"], row["quantity"])
                list_item = cls(row["name"], row["price"], row["quantity"])
                cls.all.append(list_item)

    @staticmethod
    def string_to_number(string):
        return int(float(string))
