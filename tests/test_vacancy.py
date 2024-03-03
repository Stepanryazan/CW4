import pytest
from src.Vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Программист Python", "https://hh.ru/vacancy/93374941", "Ламарт",
                   "Екатеринбург", "54000", "Применять паттерны проектирования...",
                   "Разработка качественного программного кода...")


@pytest.fixture
def vacancy_data():
    return {'name': 'Software Engineer',
            'alternate_url': 'https://example.com/vacancy/1',
            'employer': {'name': 'Company XYZ'},
            'area': {'name': 'City ABC'},
            'salary': {'from': 50000},
            'snippet': {'requirement': 'Python, Java', 'responsibility': 'Develop software'}}


def test_constructor(vacancy):
    assert vacancy.name == "Программист Python"
    assert vacancy.url == "https://hh.ru/vacancy/93374941"
    assert vacancy.employer == "Ламарт"
    assert vacancy.city == "Екатеринбург"
    assert vacancy.salary == "54000"
    assert vacancy.requirement == "Применять паттерны проектирования..."
    assert vacancy.responsibility == "Разработка качественного программного кода..."


def test_vacancies_list(vacancy_data):
    vacancy = Vacancy(
        vacancy_data['name'],
        vacancy_data['alternate_url'],
        vacancy_data['employer']['name'],
        vacancy_data['area']['name'],
        vacancy_data['salary']['from'],
        vacancy_data['snippet']['requirement'],
        vacancy_data['snippet']['responsibility']
    )
    assert vacancy in Vacancy.vacancies_list


def test_get_vacancies_by_salary():
    vacancies = {"items": [{'name': 'Vacancy 1', 'salary': {'from': 50000}},
                 {'name': 'Vacancy 2', 'salary': {'from': 60000}},
                 {'name': 'Vacancy 3', 'salary': None}]}
    sorted_vacancies = Vacancy.get_vacancies_by_salary(vacancies, 55000)
    assert len(sorted_vacancies) == 1
    assert sorted_vacancies[0]['name'] == 'Vacancy 2'


def test_get_vacancies_by_city():
    sorted_vacancies = [{'name': 'Vacancy 1', 'area': {'name': 'City A'}},
                        {'name': 'Vacancy 2', 'area': {'name': 'City B'}},
                        {'name': 'Vacancy 3', 'area': None}]
    filtered_vacancies = Vacancy.get_vacancies_by_city(sorted_vacancies, 'City A')
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]['name'] == 'Vacancy 1'