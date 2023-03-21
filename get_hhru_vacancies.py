import requests

from contextlib import suppress

from funcs import draw_table, generate_language_salary_from_hhru, LANGUAGES as languages


def process_hhru_vacancies(language):
    city_id = 1
    period = 30
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

        with suppress(requests.exceptions):
            page_response = requests.get(url, params=params)
            page_response.raise_for_status()
            page_payload = page_response.json()
            page_number = page_payload['pages']
            vacancies_on_page = page_payload['items']
            all_vacancies.extend(vacancies_on_page)
            page += 1

    return all_vacancies


def generate_hhru_table():
    all_languages_salary_table = []
    for language in languages:
        hhru_vacancies = process_hhru_vacancies(language)
        language_salary = generate_language_salary_from_hhru(language, hhru_vacancies)
        all_languages_salary_table.append(language_salary)
    table = draw_table(all_languages_salary_table, 'HeadHunter Moscow')
    return table
