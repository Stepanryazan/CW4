import json
from src.Vacancy import Vacancy, Vacancies
from src.Abstract import JSONABCSaver
import os
from config import ROOT

json_file = os.path.join(ROOT, 'data', 'hh.json')


class JSONSaver(Vacancies, JSONABCSaver):
    """
    Класс для сохранения информации о вакансиях в JSON-файл
    """

    def add_vacancy(self, vacancies):
        """
        Сохраняет вакансии в json файл
        """
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    @staticmethod
    def delete_vacancy():
        """
        Очищает json файл
        """
        pass

    def get_vacancy(self, file):
        """
        Читает json файл
        """
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
