import requests

from contextlib import suppress

from funcs import generate_language_salary_from_hhru, LANGUAGES as languages


def process_hhru_vacancies_and_generate_a_table():
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

            with suppress(requests.exceptions):
                page_response = requests.get(url, params=params)
                page_response.raise_for_status()
                page_payload = page_response.json()
                page_number = page_payload['pages']
                vacancies_on_page = page_payload['items']
                all_vacancies.extend(vacancies_on_page)
                page += 1

        language_salary = generate_language_salary_from_hhru(language, all_vacancies)
        all_languages_salary_table.append(language_salary)

    return all_languages_salary_table
