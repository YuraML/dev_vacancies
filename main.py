import os

from dotenv import load_dotenv

from funcs import draw_table
from get_superjob_vacancies import process_superjob_vacancies_and_generate_a_table
from get_hhru_vacancies import process_hhru_vacancies_and_generate_a_table


def main():
    load_dotenv()
    superjob_api_key = os.environ['SUPERJOB_API_KEY']
    hhru_vacancies = process_hhru_vacancies_and_generate_a_table()
    superjob_vacancies = process_superjob_vacancies_and_generate_a_table(superjob_api_key)
    print(draw_table(hhru_vacancies, 'HeadHunter Moscow'))
    print()
    print(draw_table(superjob_vacancies, 'SuperJob Moscow'))


if __name__ == "__main__":
    main()
