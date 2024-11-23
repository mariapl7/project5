class Vacancy:
    __slots__ = [
        "_title",
        "_url",
        "_salary",
        "_description"
    ]

    def __init__(self, title, url, salary, description):
        self._title = title
        self._url = url
        self._salary = self._validate_salary(salary)
        self._description = description

    @staticmethod
    def _validate_salary(salary):
        if salary is None or salary == "Зарплата не указана":
            return "Зарплата не указана"
        try:
            return float(salary)
        except ValueError:
            raise ValueError("Некорректное значение зарплаты")

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def salary(self):
        return self._salary

    @property
    def description(self):
        return self._description

    def __lt__(self, other):
        return self._salary < other._salary

    def __gt__(self, other):
        return self._salary > other._salary

    def __eq__(self, other):
        return self._salary == other._salary

    def __str__(self):
        return f"{self._title}: {self.salary}, {self._url}"
