import random

QUOTES = [
    "Вдохновение существует, но оно должно застать вас за работой. — Пикассо",
    "Жизнь — это 10% того, что с вами происходит, и 90% того, как вы на это реагируете. — Чарльз Суиндолл",
    "Делай сегодня то, что другие не хотят, завтра будешь жить так, как другие не могут. — Уилл Смит"
]

def get_quote():
    """Возвращает случайную цитату из списка."""
    return random.choice(QUOTES)