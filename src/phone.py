from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim_: int) -> None:
        if number_of_sim_ < 1 or number_of_sim_ % 1 != 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = number_of_sim_

    # def __repr__(self):
    #     return f'{super().__repr__()}, {self.number_of_sim}'
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other) -> int:
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise ValueError('Можно складывать только количество Item и Phone')

