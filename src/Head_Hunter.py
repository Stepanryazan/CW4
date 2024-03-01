from src.Abstract import AbstractHeadHunter
import requests


class HeadHunter(AbstractHeadHunter):
    """
    Класс для работы с API hh.ru
    """
    def get_vacancies(self, search_query, top_n):
        """
        Получение вакансий с hh.ru в формате JSON
        """
        data = requests.get(f"https://api.hh.ru/vacancies",
                            params={'text': f'{search_query}',
                                    'area': 113,
                                    'per_page': f'{top_n}'}).json()
        return data