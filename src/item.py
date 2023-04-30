import csv
from src.errors import InstantiateCSVError


class CSVChecker:
    """
    Класс для проверки целостности csv файла
    """
    def __init__(self, dict_: dict):
        if not dict_['name'] or not dict_['price'] or not dict_['quantity']:
            raise InstantiateCSVError
        else:
            self.dict_ = dict_


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    PATH_TO_CSV = 'src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.__name}'

    def __add__(self, other) -> int:
        """
        Складывание количества товара, относящегося к классам Phone или Item
        """
        if issubclass(other.__class__, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_: str) -> None:
        if len(name_) < 11:
            self.__name = name_
        else:
            raise ValueError('Name is too long.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса Item
        данными из файла src/items.csv
        """
        try:
            open(cls.PATH_TO_CSV, 'r', encoding='windows-1251')

        except FileNotFoundError:
            print('Отсутствует файл item.csv')

        else:
            with open(cls.PATH_TO_CSV, 'r', encoding='windows-1251') as file:
                csv_dict = csv.DictReader(file)

                for atr in csv_dict:
                    try:
                        CSVChecker(atr)

                    except InstantiateCSVError:
                        print('Файл item.csv поврежден')

                    else:
                        Item(atr['name'], float(atr['price']), int(atr['quantity']))

    @staticmethod
    def string_to_number(str_: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(str_))
