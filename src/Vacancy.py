class Vacancy:
    """
    Класс для работы с вакансиями
    """
    vacancies_list = []

    def __init__(self, name, url, employer, city, salary, requirement, responsibility):
        self.name = name
        self.url = url
        self.employer = employer
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility

        Vacancy.vacancies_list.append(self)

    def __str__(self):
        return (f"\nВакансия: {self.name}\n"
                f"Ссылка: {self.url}\n"
                f"Компания: {self.employer}\n"
                f"Город: {self.city}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirement}\n"
                f"Обязанности: {self.responsibility}\n")

    @classmethod
    def cast_to_object_list(cls, vacancies):
        """
        Преобразует набор данных из JSON в список объектов
        """
        for vacancy in vacancies:
            name = vacancy['name']
            url = vacancy['alternate_url']
            employer = vacancy['employer']['name']
            city = vacancy['area']['name']
            try:
                salary = vacancy['salary']['from']
            except TypeError:
                salary = vacancy['salary']
            requirement = vacancy['snippet']['requirement']
            responsibility = vacancy['snippet']['responsibility']
            cls(name, url, employer, city, salary, requirement, responsibility)

    @staticmethod
    def get_vacancies_by_salary(vacancies, salary):
        """
        Сортирует вакансии по минимальной заработной плате
        """
        sorted_salary = []
        for vacancy in vacancies['items']:
            try:
                if vacancy['salary']['from'] >= salary:
                    sorted_salary.append(vacancy)
                if vacancy['salary'] is None:
                    vacancy['salary'] = "Вакансия не найдена"
                if vacancy['salary']['from'] is None:
                    vacancy['salary']['from'] = "Вакансия не найдена"
            except TypeError:
                pass
            if salary == '':
                sorted_salary.append(vacancy)
        return sorted_salary

    @staticmethod
    def get_vacancies_by_city(sorted_salary, city):
        """
        Фильтрует вакансии по городу
        """
        filtered_salary = []
        for vacancy in sorted_salary:
            try:
                if city in vacancy['area']['name']:
                    filtered_salary.append(vacancy)
                if vacancy['area'] is None:
                    vacancy['area'] = "Вакансия не найдена"
                if vacancy['area']['name'] is None:
                    vacancy['area']['name'] = "Вакансия не найдена"
            except TypeError:
                pass
            if city == '':
                filtered_salary.append(vacancy)
        return filtered_salary

    @classmethod
    def print_vacancies(cls, vacancies_list) -> None:
        """Выводит отобранные вакансии пользователю"""
        for vacancy in vacancies_list:
            print(vacancy)