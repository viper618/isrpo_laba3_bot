from jokes import get_joke  # Импорт функции для получения анекдота

def main():
    print("Добро пожаловать в Joke Bot! 🤖")
    print("Введите 'joke', чтобы получить анекдот, или 'exit', чтобы выйти.\n")

    while True:
        command = input("👉 Ваш выбор: ").strip().lower()
        if command == "joke":
            print("\n" + get_joke() + "\n")
        elif command == "exit":
            print("Спасибо за использование Joke Bot! До встречи! 👋")
            break
        else:
            print("❌ Неизвестная команда. Попробуйте снова.\n")

if __name__ == "__main__":
    main()

from jokes import get_joke
from quotes import get_quote

if command == "joke":
    print("\n" + get_joke() + "\n")
elif command == "quote":
    print("\nЦитата дня:\n" + get_quote() + "\n")

