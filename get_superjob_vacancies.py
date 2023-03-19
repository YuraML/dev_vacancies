import requests

from contextlib import suppress

from funcs import generate_language_salary_from_superjob, LANGUAGES as languages


def process_superjob_vacancies_and_generate_a_table(superjob_api_key):
    all_languages_salary_table = []
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': superjob_api_key}

    for language in languages:
        all_vacancies = []
        vacancies_count = 20
        city_id = 4
        profession_id = 48
        page = 0
        page_number = 1

        while page < page_number:
            params = {'town': city_id,
                      'catalogues': profession_id,
                      'page': page,
                      'keyword': language,
                      'count': vacancies_count
                      }
            with suppress(requests.exceptions):
                page_response = requests.get(url, headers=headers, params=params)
                page_response.raise_for_status()
                page_payload = page_response.json()
                vacancies_in_total = page_payload['total']

                if vacancies_in_total < vacancies_count:
                    page_number = 1
                else:
                    page_number = vacancies_in_total // vacancies_count
                vacancies_on_page = page_payload['objects']

                for vacancy in vacancies_on_page:
                    all_vacancies.append(vacancy)
                page += 1

        language_salary = generate_language_salary_from_superjob(language, all_vacancies)
        all_languages_salary_table.append(language_salary)

    return all_languages_salary_table
