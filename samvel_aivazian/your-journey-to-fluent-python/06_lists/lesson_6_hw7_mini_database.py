import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class MiniDatabase:
    def __init__(self):
        self.data = []

    def add_person(self, name, age, hobbies, favorite_foods):
        person = {
            'Name': name,
            'Age': age,
            'Hobbies': hobbies.split(', '),
            'Favorite Foods': favorite_foods.split(', ')
        }
        self.data.append(person)
        logging.info("Personal Information:")
        for key, value in person.items():
            logging.info(f"{key}: {value}")


def main():
    db = MiniDatabase()
    logging.info("Enter your name: ")
    name = input().strip()
    logging.info("Enter your age: ")
    age = input().strip()
    logging.info("Enter your hobbies (separated by commas): ")
    hobbies = input().strip()
    logging.info("Enter your favorite foods (separated by commas): ")
    favorite_foods = input().strip()

    db.add_person(name, age, hobbies, favorite_foods)


if __name__ == "__main__":
    main()
