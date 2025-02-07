# Проект Курсовая 2

## Описание:

Проект Курсовая 2 - Поиск вакансий

## Содержание проекта:

1. Модуль main.py:
1.1 Создание класса HeadHunterAPI:
1.1.1 Создание функции get_vacancies - получение вакансий.
1.1.2 Создание функции user_interface - интерфейс взаимодействия с пользователем.
2. Модуль api.py:
2.1 Создание абстрактного класса AbstractAPI(ABC).
2.2 Создание абстрактного класса HeadHunterAPI(AbstractAPI):
2.2.1 Создание функции get_vacancies - получение вакансий по ключевому слову.
3. Модуль models.py:
3.1 Создание класса Vacancy.
4. Модуль file_saver.py.
4.1 Создание абстрактного класса AbstractFileHandler(ABC).
5. Модуль вспомогательный utils.py.
5.1 Создание функции load_json_file - загружает данные из JSON-файла. Если файл не найден, возвращает пустой список
5.2 Создание функции save_json_file - сохраняет данные в JSON-файл.
5.3 Создание функции is_duplicate - проверяет наличие дубликата по заголовку вакансии.

## Тестирование:

1. Тестирование для функции test_main.
2. Тестирование для функции test_saver.
3. Тестирование для функции test_utils.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://git@github.com:mariapl7/project5.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Запустите проект на своем IDE.
3. Проведите все необходимые проверки.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
