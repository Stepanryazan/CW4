from src.Vacancy import Vacancy
from src.HeadHunter import HeadHunter
from src.JSONSaver import JSONSaver
import os
from config import ROOT


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    search_query = str(input("Введите поисковый запрос: "))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    city = str(input("Введите город: "))
    salary = int(input("Введите минимальную зарплату: "))
    hh_api = HeadHunter()
    hh_vacancies = hh_api.get_vacancies(search_query, top_n)
    hh_json = JSONSaver()
    hh_json.add_vacancy(hh_vacancies)
    json_file = os.path.join(ROOT, 'data', 'hh.json')
    data = hh_json.get_vacancy(json_file)
    ranged_vacancies = Vacancy.get_vacancies_by_salary(data, salary)
    filtered_salary = Vacancy.get_vacancies_by_city(ranged_vacancies, city)
    Vacancy.cast_to_object_list(filtered_salary)
    if not Vacancy.vacancies_list:
        print("\nПодходящих вакансий не найдено")
    else:
        print("\nСписок подходящих вакансий: ")
        Vacancy.print_vacancies(Vacancy.vacancies_list)