from jokes import get_joke  # Импорт функции для получения анекдота
from quotes import get_quote # Импорт функции для получения цитаты
from tips import get_tip # Импорт функции для получения совета

def main():
    print("Добро пожаловать в Joke Bot! 🤖")
    print("Введите 'joke', чтобы получить анекдот, 'quote' — цитату дня, 'tip' — совет дня или 'exit', чтобы выйти.\n")

    while True:
        command = input("👉 Ваш выбор: ").strip().lower()
        if command == "joke":
            print("\n" + get_joke() + "\n")
        elif command == "quote":
            print("\nЦитата дня:\n" + get_quote() + "\n")
        elif command == "tip":
            print("\nСовет дня:\n" + get_tip() + "\n")
        elif command == "exit":
            print("Спасибо за использование Joke Bot! До встречи! 👋")
            break
        else:
            print("❌ Неизвестная команда. Попробуйте снова.\n")
        

if __name__ == "__main__":
    main()
