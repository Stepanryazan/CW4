from src.HeadHunter import HeadHunter
import pytest


def test_get_vacancies():
    assert ((HeadHunter.get_vacancies(HeadHunter(), "python", 1))['items'][0]['name']
            == "Стажер-разработчик Python")
    assert ((HeadHunter.get_vacancies(HeadHunter(), "python", "python"))['description']
            == "can't convert page argument to positive integer")