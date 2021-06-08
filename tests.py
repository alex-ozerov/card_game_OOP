from cards_game import Card, CardDeck


def main():
    # Создание пустой колоды карт
    card_deck = CardDeck(suits={'Hearts', 'Diamonds', 'Clubs', 'Spades'},
                         values={'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'})

    print('Попытка добавить испорченную карту в колоду:')
    Card(suit='Spades', deck=card_deck)

    # Добавление карт в колоду
    Card(suit='Spades', value=10, deck=card_deck)
    Card(suit='Spades', value='Q', deck=card_deck)
    Card(suit='Spades', value='K', deck=card_deck)
    Card(suit='Spades', value='2', deck=card_deck)

    print('\nПопытка добавить дубликат карты в колоду:')
    Card(suit='Spades', value='2', deck=card_deck)
    # Result: deck cannot contain two copy of the card
    print('\nКолода карт содержит:')
    print(card_deck)
    # Перетасовать колоду
    card_deck.shuffle_deck()
    print('\nПеретасованная колода карт:')
    print(card_deck)
    # Достать из колоды верхнюю карту
    card = card_deck.withdraw_card()
    print('\nКарта, которую достали сверху колоды:')
    print(card)
    print('\nВ колоде остались такие карты:')
    print(card_deck)
    # Достать из колоды руку карт для игры
    card_set = card_deck.withdraw_card(2)
    print('\nРука карт для игры:')
    print(card_set)
    print('\nВ колоде остались такие карты:')
    print(card_deck)
    # Достать из колоды нужную карту, перебрав всю колоду:
    print('\nДостать нужную карту из колоды:')
    card = card_deck[0]
    print(card.withdraw_card())
    print('\nВ колоде остались такие карты:')
    print(card_deck)


if __name__ == '__main__':
    main()
