from src.item import Item


class MixinLang:
    """
    Класс-миксин, который содержит функционал по хранению и изменению раскладки клавиатуры
    """
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Метод, изменяющий раскладку клавиатуры. Всего поддерживается два языка: EN и RU
        """
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для товара “клавиатура”.
    """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
