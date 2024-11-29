import random

TIPS = [
    "Пейте больше воды — это поможет сохранить энергию и улучшить концентрацию.",
    "Не забывайте про зарядку утром — это задаст тонус на весь день.",
    "Выделите время для чтения книг — это помогает развивать мозг и расслабляться.",
    "Делайте паузы в работе каждые 50 минут, чтобы оставаться продуктивным.",
    "Планируйте день заранее — это экономит время и уменьшает стресс."
]

def get_tip():
    """Возвращает случайный совет из списка."""
    return random.choice(TIPS)