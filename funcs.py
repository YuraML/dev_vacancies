from terminaltables import AsciiTable


LANGUAGES = ["Python", "Javascript", "Java", "1C", "PHP", "C++", "C#", "C", "Go"]


def get_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    elif salary_from and not salary_to:
        return int(salary_from * 1.2)
    elif not salary_from and salary_to:
        return int(salary_to * 0.8)
    else:
        return None


def predict_rub_salary_for_superjob(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    return get_salary(salary_from, salary_to)


def predict_rub_salary_for_hhru(vacancy):
    salary = vacancy['salary']
    if not salary or salary['currency'] != 'RUR':
        return None
    salary_from = salary['from']
    salary_to = salary['to']
    return get_salary(salary_from, salary_to)


def generate_language_salary_from_hhru(language, all_vacancies):
    salaries = []
    vacancies_in_total = len(all_vacancies)
    salaries_in_total = 0

    for vacancy in all_vacancies:
        salary_hh = predict_rub_salary_for_hhru(vacancy)
        if salary_hh:
            salaries.append(salary_hh)
            salaries_in_total += salary_hh

    processed_salaries = len(salaries)
    language_average_salary = {
        language: {
            "vacancies_found": vacancies_in_total,
            "vacancies_processed": processed_salaries,
            "average_salary": int(salaries_in_total / processed_salaries) if processed_salaries else None
        }
    }
    return language_average_salary


def generate_language_salary_from_superjob(language, all_vacancies):
    salaries = []
    vacancies_in_total = len(all_vacancies)
    salaries_in_total = 0

    for vacancy in all_vacancies:
        salary_superjob = predict_rub_salary_for_superjob(vacancy)
        if salary_superjob:
            salaries.append(salary_superjob)
            salaries_in_total += salary_superjob

    processed_salaries = len(salaries)
    language_average_salary = {
        language: {
            "vacancies_found": vacancies_in_total,
            "vacancies_processed": processed_salaries,
            "average_salary": int(salaries_in_total / processed_salaries) if processed_salaries != 0 else None
        }
    }
    return language_average_salary


def draw_table(all_languages_salary_table, title):
    raw_table = [
        [
            "Язык программирования",
            "Найдено вакансий",
            "Обработано вакансий",
            "Средняя зарплата",
        ]
    ]

    for language_vacancies in all_languages_salary_table:
        for language, vacancies in language_vacancies.items():
            raw_table.append(
                [
                    language,
                    vacancies['vacancies_found'],
                    vacancies['vacancies_processed'],
                    vacancies['average_salary'],

                ]
            )
    table_instance = AsciiTable(raw_table, title)
    return table_instance.table
