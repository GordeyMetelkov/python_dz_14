import json
import os


class User:

    def __init__(self, name: str, the_id: str, level='1'):
        if not name.isalpha():
            raise ValueError("Имя должно состять только из букв")
        if not the_id.isdigit():
            raise ValueError("ID должен состоять только из цифр")
        if not level.isdigit() or int(level) not in range(1, 8):
            raise ValueError("Уровень должен целым числом от 1 до 7")
        self.name = name.title()
        self.the_id = int(the_id)
        self.level = int(level)

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'

    def __eq__(self, other):
        if isinstance(other, User):
            return all((self.name == other.name, self.the_id == other.the_id))

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data

def worker():
    while True:
        try:
            name = input("Ведите имя: ")
            the_id = input("Введите ID: ")
            level = input("Введите уровень: ")
            return User(name, the_id, level)
        except ValueError as e:
            print(e)
def save_json(path, user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)