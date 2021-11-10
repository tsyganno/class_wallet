class Wallet:
    def __init__(self, currency, balance):
        self.balance = balance
        if isinstance(currency, str) == False:
            raise TypeError('Неверный тип валюты')
        elif len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif currency.isupper() == False:
            raise ValueError('Название должно состоять только из заглавных букв')
        else:
            self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return self.balance == other.balance
            else:
                raise ValueError('Нельзя сравнить разные валюты')
        else:
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        else:
            raise ValueError('Данная операция запрещена')

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        else:
            raise ValueError('Данная операция запрещена')