from abc import ABC, abstractmethod


class AbstractHeadHunter(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, search_query, top_n):
        pass


class JSONABCSaver(ABC):
    """
    Запись полученных вакансий в файл json и чтение
    """

    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def get_vacancy(self, file):
        pass
