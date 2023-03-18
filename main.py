from get_superjob_vacancies import get_superjob_vacancies
from get_hhru_vacancies import get_hhru_vacancies


def main():
    hhru_vacancies = get_hhru_vacancies()
    superjob_vacancies = get_superjob_vacancies()
    print(hhru_vacancies)
    print()
    print(superjob_vacancies)


if __name__ == "__main__":
    main()
