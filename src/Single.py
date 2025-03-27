import csv
import json


# 1. Чтение данных из books.csv
def read_books(file_path):
    books = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Преобразуем числовые поля в соответствующие типы
            row["Pages"] = int(row["Pages"])
            books.append(row)
    return books


# 2. Чтение данных из users.json
def read_users(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        users = json.load(file)
    return users


# 3. Распределение книг между пользователями
def distribute_books(users, books):
    num_users = len(users)
    num_books = len(books)

    # Вычисляем базовое количество книг на пользователя и остаток
    base_books_per_user = num_books // num_users
    extra_books = num_books % num_users
    result = []
    book_index = 0

    for i, user in enumerate(users):
        # Копируем данные пользователя
        user_data = {
            "name": user.get("name", ""),
            "gender": user.get("gender", ""),
            "address": user.get("address", ""),
            "age": user.get("age", 0),
            "books": [],
        }

        # Определяем количество книг для текущего пользователя
        books_for_user = base_books_per_user + (1 if i < extra_books else 0)

        # Добавляем книги пользователю
        for _ in range(books_for_user):
            if book_index < num_books:
                user_data["books"].append(books[book_index])
                book_index += 1

        result.append(user_data)

    return result


# 4. Сохранение результата в файл result.json
def save_result(file_path, data):
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Основная функция
def main():
    # Пути к файлам
    books_file = "files/books.csv"
    users_file = "files/users.json"
    result_file = "result.json"

    # Чтение данных
    books = read_books(books_file)
    users = read_users(users_file)

    # Распределение книг
    result = distribute_books(users, books)

    # Сохранение результата
    save_result(result_file, result)

    print(f"Результат успешно сохранён в файл {result_file}")


# Запуск скрипта
if __name__ == "__main__":
    main()
