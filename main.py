from dotenv import load_dotenv


from get_superjob_vacancies import generate_superjob_table
from get_hhru_vacancies import generate_hhru_table


def main():
    load_dotenv()
    hhru_vacancies = generate_hhru_table()
    superjob_vacancies = generate_superjob_table()
    print(hhru_vacancies)
    print()
    print(superjob_vacancies)


if __name__ == "__main__":
    main()
