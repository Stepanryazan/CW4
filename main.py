from src.UserInteraction import UserInteraction


def main():
    user_input = input("Введите поисковый запрос: ")

    while True:
        users_salary = input("Отправьте сообщение о зарплате, если хотите\n"
                             "посмотреть вакансии с зарплатой:\n")
        if users_salary.isdigit():
            break
        print("\nПожалуйста, напишите число и нажмите Enter...\n")

    user = UserInteraction(user_input)

    while True:
        users_city = input("Введите город:\n").capitalize()
        if users_city.isalpha():
            break
        print("\nЯ не знаю такого города.\n")

    user.sorted_salary(user.all_vacancy, int(users_salary), users_city)
    user.get_top_vacancies(user.sort_salary)

    user.make_info(user.top_salary)

    while True:
        number_vacancy = input("Выберите количество топовых вакансий\n"
                               "если хотите увидеть больше: ")
        if number_vacancy.isdigit():
            break

    print(user.last_info(user.vacancies_list, number_vacancy))


if __name__ == '__main__':
    main()