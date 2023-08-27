from src.item import Item


class MixLog:
    language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"

        elif self.language == "RU":
            self.language = "EN"

        else:
            raise AttributeError(
                "property 'language' of 'Keyboard' object has no setter"
            )

        return self


class Keyboard(Item, MixLog):
    pay_rate = 1.0

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}"
