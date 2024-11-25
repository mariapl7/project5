import requests
from src.utils import load_json_file, save_json_file, is_duplicate


class HeadHunterAPI:
    """Класс для взаимодействия с API HeadHunter."""

    @staticmethod
    def get_vacancies(search_query):
        """Получает список вакансий по заданному запросу."""
        url = f'https://api.hh.ru/vacancies?text={search_query}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['items']  # Вернем список вакансий
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []


def user_interface():
    """Интерфейс взаимодействия с пользователем.

    Позволяет пользователю выполнять различные действия, связанные с вакансиями,
    такие как просмотр, добавление и удаление вакансий.
    """
    filename = "data.json"
    hh_api = HeadHunterAPI()

    while True:
        print("\nВыберите действие:")
        print("1. Показать вакансии")
        print("2. Добавить вакансию")
        print("3. Удалить вакансию")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            # Получаем вакансии с API
            vacancies = hh_api.get_vacancies("Python")
            print("Список вакансий:")
            for v in vacancies:
                salary = v['salary'] if v['salary'] else "Не указана"
                print(f"- {v['name']}: {salary} (Ссылка: {v['alternate_url']})")

        elif choice == '2':
            title = input("Введите заголовок вакансии: ")
            salary = input("Введите зарплату: ")
            new_vacancy = {"title": title, "salary": salary}

            existing_data = load_json_file(filename)
            if not is_duplicate(existing_data, title):
                existing_data.append(new_vacancy)
                save_json_file(filename, existing_data)
                print("Вакансия добавлена.")
            else:
                print("Вакансия с таким заголовком уже существует.")

        elif choice == '3':
            title = input("Введите заголовок вакансии для удаления: ")
            existing_data = load_json_file(filename)
            updated_data = [item for item in existing_data if item['title'] != title]
            save_json_file(filename, updated_data)
            print("Вакансия удалена, если она существовала.")

        elif choice == '4':
            print("Выход...")
            break

        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    user_interface()
