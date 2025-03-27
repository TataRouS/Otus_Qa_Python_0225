import json


def make_result(users, books):
    num_users = len(users)
    num_books = len(books)
    books_per_user = num_books // num_users
    extra_books = num_books % num_users
    results = []
    book_index = 0
    i = 0
    for user in users:
        result = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [
            ]
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

def Usersbook

# чНаписать скрипт, который из двух данных файлов будет читать
# данные и на их основании создаст файл result.json в следующем
# формате
#

# {'Title': 'Journal of Economics, vol 106 No 3', 'Author': '', 'Genre': 'economics', 'Pages': '235', 'Publisher': ''}
#
# {'_id': '5e2696e561fdc6df60d43b5f', 'index': 0, 'guid': '3e518b31-20f0-4dea-8de8-039af5afbd33', 'isActive': False,
#  'balance': '$3,646.47', 'picture': 'http://placehold.it/32x32', 'age': 34, 'eyeColor': 'brown', 'name': 'Lolita Lynn',
#  'gender': 'female', 'company': 'HIVEDOM', 'email': 'lolitalynn@hivedom.com', 'phone': '+1 (842) 513-2979',
#  'address': '389 Neptune Avenue, Belfair, Iowa, 6116',
#  'about': 'Ea irure labore culpa proident sint cupidatat minim laboris labore eu exercitation aliqua duis aute. Consectetur pariatur commodo enim pariatur mollit. Laborum nisi cillum do consectetur laboris nulla id laboris eu voluptate sit consequat commodo aute. Ad minim eiusmod pariatur non cupidatat esse fugiat et laborum ullamco commodo. Sint fugiat enim elit pariatur consequat ipsum Lorem qui qui Lorem proident mollit culpa. In enim commodo culpa nostrud reprehenderit nostrud incididunt elit labore. Aute proident mollit pariatur proident enim commodo.\r\n',
#  'registered': '2014-03-19T10:39:24 -06:00', 'latitude': 0.246756, 'longitude': -96.404056,
#  'tags': ['ad', 'ut', 'do', 'dolor', 'qui', 'quis', 'enim'],
#  'friends': [{'id': 0, 'name': 'Joan Weaver'}, {'id': 1, 'name': 'Morris Wheeler'}, {'id': 2, 'name': 'Morton Noble'}],
#  'greeting': 'Hello, Lolita Lynn! You have 2 unread messages.', 'favoriteFruit': 'banana'}

# [
#     {
#         "name": "Lolita Lynn",
#         "gender": "female",
#         "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
#         "age": 34,
#         "books": [
#             {
#                 "title": "Fundamentals of Wavelets",
#                 "author": "Goswami, Jaideva",
#                 "pages": 228,
#                 "genre": "signal_processing"
#             }
#         ]
#     },
# ]
