import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.massage = "InstantiateCSVError: Файл item.csv поврежден"


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

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

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
    def instantiate_from_csv(
        cls, file_name="/Users/a1/SkyPro/electronics-shop-project/src/items.csv"
    ):
        try:
            with open(file_name, newline="") as csfile:
                reader = csv.DictReader(csfile)
                for row in reader:
                    try:
                        # print(row["name"], row["price"], row["quantity"])
                        list_item = cls(row["name"], row["price"], row["quantity"])

                        if (
                            row["name"] == ""
                            or row["price"] == ""
                            or row["quantity"] == ""
                        ):
                            raise InstantiateCSVError

                    except InstantiateCSVError as ex:
                        print(ex.massage)

                    cls.all.append(list_item)

        except FileNotFoundError:
            print(f"FileNotFoundError: Отсутствует файл {file_name}")

    @staticmethod
    def string_to_number(string):
        return int(float(string))
