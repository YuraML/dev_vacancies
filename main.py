from dotenv import load_dotenv


from funcs import draw_table
from get_superjob_vacancies import formalize_all_vacanices_for_superjob_table
from get_hhru_vacancies import formalize_all_vacanices_for_hhru_table


def main():
    load_dotenv()
    hhru_formalized_vacancies = formalize_all_vacanices_for_hhru_table()
    hhru_vacancies_table = draw_table(hhru_formalized_vacancies, 'HeadHunter Moscow')
    superjob_formalized_vacancies = formalize_all_vacanices_for_superjob_table()
    superjob_vacancies_table = draw_table(superjob_formalized_vacancies, 'SuperJob Moscow')
    print(hhru_vacancies_table)
    print()
    print(superjob_vacancies_table)


if __name__ == "__main__":
    main()
