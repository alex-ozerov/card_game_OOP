import random


class CardDeck:
    # Указание будущих атрибутов экземпляра класса
    __slots__ = ('__cards', '__suits', '__values')

    # Инициализация атрибутов экземпляра класса
    def __init__(self, suits, values):
        self.__cards = []
        self.__suits = suits
        self.__values = values

    # Определение строкового представления объекта
    def __repr__(self):
        return f'CardDeck({", ".join(map(str, self.cards))})'

    # Определение метода индексации
    def __getitem__(self, index):
        try:
            return self.cards[index]
        except (IndexError, ValueError, TypeError) as e:
            print(e)

    # Определение проверки длины колоды карт
    def __len__(self):
        return len(self.cards)

    # Определение проверки на наличие карты в колоде
    def __contains__(self, item):
        for i in self.cards:
            if item.value == i.value and item.suit == i.suit:
                return True
        else:
            return False

    # Взять верхнюю карту из колоды
    def __withdraw_card_from_top(self):
        try:
            card = self.cards.pop()
        except ValueError:
            print('deck is empty')
        else:
            return card

    # Взять набор карт сверху из колоды
    def __withdraw_card_set(self, count):
        try:
            if count > len(self):
                raise IndexError('the deck hasn\'t so much cards')
            elif count < 1:
                raise IndexError('card set length must be at least 1')
        except IndexError as e:
            print(e)
        else:
            return [self.__withdraw_card_from_top() for x in range(0, count)]

    # Публичный метод-интерфейс для запуска скрытых методов
    def withdraw_card(self, value=None):
        if type(value) is int:
            return self.__withdraw_card_set(value)
        elif value is not None:
            print('Please enter a number of play cards')
        else:
            return self.__withdraw_card_from_top()

    # Перетасовать колоду карт
    def shuffle_deck(self):
        random.shuffle(self.cards)

    @property
    def suits(self):
        return self.__suits

    @property
    def values(self):
        return self.__values

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        if value.__class__.__bases__[0] is type(self):
            self.cards.append(value)
        else:
            raise ValueError('this is not a card')


class Card(CardDeck):
    # Указание будущих атрибутов экземпляра класса
    __slots__ = ('__suit', '__value', '__card_deck')

    # Инициализация атрибутов экземпляра класса
    def __init__(self, **kwargs):
        # Определение атрибутов из словаря именованных параметров
        try:
            self.__card_deck = kwargs['deck']
            self.__suit = kwargs['suit']
            self.__value = str(kwargs['value'])
        except KeyError:
            print('Please enter suit, value and deck')
        else:
            # Проверки на валидность созданной карты
            try:
                # Является ли переданный объект колоды карт - колодой карт?
                if not isinstance(self.card_deck, self.__class__.__bases__[0]):
                    raise TypeError('it is not a deck')
                # Допустима ли указанная масть для указанной колоды карт?
                elif self.suit not in self.card_deck.suits:
                    raise ValueError('wrong card suit')
                # Допустимо ли указанное значение для указанной колоды карт?
                elif self.value not in self.card_deck.values:
                    raise ValueError('wrong card value')
                # Есть ли уже такая карта в указанной колоде карт?
                elif self in self.card_deck:
                    raise ValueError('deck cannot contain two copy of the card')
            except (ValueError, TypeError) as e:
                print(e)
            else:
                # Добавление валидной карты в колоду карт (через сеттер)
                self.card_deck.cards = self

    # Определение строкового представления объекта
    def __repr__(self):
        return f'Card({self.suit}, {self.value})'

    # Определение операции равенства двух карт
    def __eq__(self, value):
        return all((self.suit == value.suit, self.value == value.value))

    # Определение длины объекта карты
    def __len__(self):
        return 1

    # Определение проверки на масть и значение карты
    def __contains__(self, item):
        return any((self.value == item, self.suit == item))

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, value):
        self.__suit = value

    @suit.deleter
    def suit(self):
        self.__suit = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @value.deleter
    def value(self):
        self.__value = None

    @property
    def card_deck(self):
        return self.__card_deck

    # Взять указанную карту из колоды карт
    def withdraw_card(self, value=None):
        try:
            self.card_deck.cards.remove(self)
        except ValueError:
            print('deck does not contain this card')
        else:
            return self

    # Перетасовать колоду карт -
    # перенаправление на родительский метод
    def shuffle_deck(self):
        self.card_deck.shuffle_deck()
