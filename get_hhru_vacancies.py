import requests

from contextlib import suppress

from funcs import generate_language_salary_from_hhru, LANGUAGES as languages


def process_hhru_vacancies(language):
    city_id = 1
    period = 30
    all_vacancies = []
    url = 'https://api.hh.ru/vacancies'
    page = 0
    page_number = 1

    while page < page_number:
        params = {
            'text': language,
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


def formalize_all_vacanices_for_hhru_table():
    all_languages_formalized_vacanices = []
    for lang in languages:
        hhru_vacs = process_hhru_vacancies(lang)
        language_salary = generate_language_salary_from_hhru(lang, hhru_vacs)
        all_languages_formalized_vacanices.append(language_salary)
    return all_languages_formalized_vacanices
