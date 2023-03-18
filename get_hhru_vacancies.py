import requests

from funcs import draw_table, get_language_salary, languages


def get_hhru_vacancies():
    title = 'HeadHunter Moscow'
    all_languages_salary_table = []
    city_id = 1
    period = 30

    for language in languages:
        all_vacancies = []
        url = 'https://api.hh.ru/vacancies'
        page = 0
        page_number = 1

        while page < page_number:
            params = {'text': language,
                      'area': city_id,
                      'period': period,
                      'page': page
                      }
            try:
                page_response = requests.get(url, params=params)
                page_response.raise_for_status()
                page_payload = page_response.json()
                page_number = page_payload['pages']
                vacancies_on_page = page_payload['items']
                for vacancy in vacancies_on_page:
                    all_vacancies.append(vacancy)
                page += 1
            except requests.exceptions:
                continue

        language_salary = get_language_salary(language, all_vacancies, title)
        all_languages_salary_table.append(language_salary)

    return draw_table(all_languages_salary_table, title)
