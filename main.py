from get_superjob_vacancies import get_superjob
from get_hhru_vacancies import get_hhru


def main():
    hhru_vacancies = get_hhru()
    superjob_vacancies = get_superjob()
    print(hhru_vacancies)
    print()
    print(superjob_vacancies)


if __name__ == "__main__":
    main()
