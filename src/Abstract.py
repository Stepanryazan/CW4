from abc import ABC, abstractmethod


class AbstractHeadHunter(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, search_query, top_n):
        pass