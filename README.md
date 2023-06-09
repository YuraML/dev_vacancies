# dev_vacancies
 
Программа выводит таблицы со средней зарплатой разработчиков разных языков программирования в городе Москва. Данные берутся  с помощью API из вакансий с сайтов объявлений [HeadHunter](https://hh.ru/) и [SuperJob](https://www.superjob.ru/).

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Также необходим файл `.env`, заполненный следующим образом:

```
SUPERJOB_API_KEY="ваш токен"
```

Для работы API SuperJob необходим токен. Получить его вы можете [здесь](https://api.superjob.ru/).


### Запуск

Для запуска введите в командную строку:

```console
python main.py
```

Скрипт выводит две таблицы с зарплатами с сайтов HeadHunter и SuperJob. После запуска необходимо подождать несколько минут, так как в процессе обрабатывается большое количество данных.

### Содержимое

`get_hhru_vacancies.py` - обрабатывает вакансии с HeadHunter и формирует таблицу со средними зарплатами 10 популярных языков программирования.

`get_superjob_vacancies.py` - то же, что и выше, но с вакансиями с SuperJob

`funcs.py` - различные функции, необходимые для работы скрипта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).