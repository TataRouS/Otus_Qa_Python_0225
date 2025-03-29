from files import RESULT_FILE_PATH
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from src.csv_reader import read_csv
from src.json_reader import read_json
from src.json_write import write_json


def make_result(users, books):
    num_users = len(users)
    num_books = len(books)
    books_per_user = num_books // num_users
    extra_books = num_books % num_users
    results = []
    i = 0
    for user in users:
        result = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
        books_count = books_per_user
        if i < extra_books:
            books_count = books_count + 1
        books_for_user = books[0:books_count]
        for book in books_for_user:
            result_book = {
                "title": book.get("Title", ""),
                "author": book.get("Author", ""),
                "pages": book.get("Pages", ""),
                "genre": book.get("Genre", ""),
            }
            result["books"].append(result_book)
        results.append(result)
    print(results)
    return results


def usersbook_distribute():
    books = read_csv(CSV_FILE_PATH)
    users = read_json(JSON_FILE_PATH)
    result = make_result(users, books)
    write_json(RESULT_FILE_PATH, result)
    print("Json is ready")


if __name__ == "__main__":
    usersbook_distribute()
