# tjas-erp

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg?label=Status)](./README.md)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Ftjas-erp&count_bg=%2379C83D&title_bg=%23555555&title=Hits&edge_flat=false)](https://hits.seeyoufarm.com)
![Coverage](https://img.shields.io/badge/coverage-76%25-yellow?label=Test%20coverage)
[![Licence](https://img.shields.io/github/license/tjas/tjas-erp?color=orange&label=Licence)](https://github.com/tjas/tjas-erp/blob/master/LICENCE)
[![Commits](https://img.shields.io/github/commit-activity/t/tjas/tjas-erp?label=Commits)](https://github.com/tjas/tjas-erp/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/tjas/tjas-erp?color=blue&label=Last%20commit)
![Repo size](https://img.shields.io/github/repo-size/tjas/tjas-erp?color=888888&label=Repo%20size)
![Code size](https://img.shields.io/github/languages/code-size/tjas/tjas-erp?color=888888&label=Code%20size)
[![Stars](https://img.shields.io/github/stars/tjas/tjas-erp?color=blue&label=Stars)](https://github.com/tjas/tjas-erp/stargazers)
[![Watchers](https://img.shields.io/github/watchers/tjas/tjas-erp?color=blue&label=Watchers)](https://github.com/tjas/tjas-erp/watchers)
[![Forks](https://img.shields.io/github/forks/tjas/tjas-erp?color=blue&label=Forks)](https://github.com/tjas/tjas-erp/forks)

[![Python](https://img.shields.io/badge/python-v3.10.11-darkgreen?label=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-v4.2.1-green?label=Djando)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-v15.3.0-blue?label=PostgreSQL)](https://www.postgresql.org/)

> ⭐ Mark the project with a star. 👀 Watch the project for receive news.
>
> 🇧🇷 Acesse esta página em [Português do Brasil](./README_pt-br.md).
<!-- >
> 🌐 Access my personal website: [thiago-tjas.com](http://thiago-tjas.com/) -->

Advanced Python/Django ERP application for product, employee and sales registration, detailing, editing, deletion and listing, with access control. Features and evolutions planned can be found in the [Main Features Available](#main-features-available) section.

<!-- 
## Build With

* Python 3.10.11
* Django 4.2.1
* PostgreSQL 15.3.0 
-->

## Main Features Available

> To learn more about upcoming releases, refer to the [Project Roadmap](https://github.com/users/tjas/projects/2/views/1)

* Employees' registration, detailing, editing and listing;
* Products' registration, detailing, editing, deletion and listing;
* Sales' registration, detailing, editing, deletion and listing;
* Public and private pages access control;
* Connection to persist informations in local data base;
* 76% of test coverage.

<!-- 
* Create rich user interface with [Bootstrap](https://getbootstrap.com/);
* Create new product, employee and sale's fields and categories;
* Create products' stock control;
* Create stores' registration, detailing, editing, deletion and listing;
* Create link between stores and employees;
* Create stores' public and restrict access pages;
* Create customers' registration, detailing, editing and listing;
* Create customers' rich shopping page;
* Create customers' shopping cart;
* Create customers' following store list;
* Create customers' favorites list;
* Create customers' purchase history page;
* Create customers' shipping address page;
* Create customers' payment method page;
* Create purchase steps with payment method and delivery address;
* Create pagination in listing views;
* Create filters in listing views;
* Create translation to other languages. 
-->

## Getting Started

This is an example of how you may set up the project locally in your computer. We strongly recommended that you use virtual environments to run the application, we recommend [Virtualenv](https://virtualenv.pypa.io/en/latest/) (or any other of your choice). Read it, create and activate the virtual environment inside the project folder before steps 5.

To get a local copy up and running follow these steps:

1. Make sure you have Python 3.10.11+ installed or do it from [Python.org](https://www.python.org/) or from [Anaconda](https://www.anaconda.com/);
2. Make sure you have Git installed or do it from [Git-scm.com](https://git-scm.com/);
3. Access the folder you want to save the project, then clone the repo there
    ```sh
    git clone https://github.com/tjas/tjas-erp
    ```
4. Access the project folder;
5. Install the project dependencies
   ```py
   pip install -r requirements.txt
   ```
6. Make sure [PostgreSQL](https://www.postgresql.org/) is running on your computer and that the ```db_erp``` database has been created. The database name, access and other related settings must be verified and can be changed in the ```DATABASES``` variable of ```settings.py``` file, located in main application folder (```core``` module).
7. Run the migrations
    ```py
    python manage.py migrate
    ```
8. Run Django project
    ```py
    python manage.py runserver
    ```
9. Then access aplication at <http://127.0.0.1:8000/>

## Contributing
<!-- > Adapted from the ["Flappy Bird: Dev Soutinho"](https://github.com/omariosouto/flappy-bird-devsoutinho/blob/master/CONTRIBUTING.md) project. -->

1. Fork it!
2. Create your feature branch:
    ```sh
    git checkout -b my-new-feature
    ```
3. Add files changed:
    ```sh
    git add .
    ```
4. Commit your changes:
    ```sh
    git commit -m "Add some useful comment here"
    ```
5. Push to the branch:
    ```sh
    git push origin my-new-feature
    ```
6. Submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    * Add a title and description that let clear your suggestion;
    * Use the English language for comments and branch names;
    * After your pull request is merged, you can safely delete your branch.

## Tests

For unit testing creation it was been used the tools available in the [```django.test```](https://docs.djangoproject.com/pt-br/4.2/topics/testing/) module of Django and in [unittest](https://docs.python.org/3/library/unittest.html) library of Python. To assess test coverage, the [coverage](https://pypi.org/project/coverage/) package was used.

### Performing the Tests

From inside the project folder, run:

```sh
python manage.py test
```

### Checking Tests Coverage

From inside the project folder, run the tool and generate reports:

```sh
coverage run --omit='*/venv/*' manage.py test
coverage report
coverage html
```

## Contact

**Thiago Jorge Almeida dos Santos**, project author and maintainer.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logoColor=white&link=https://www.linkedin.com/in/thiago-tjas)](https://www.linkedin.com/in/thiago-tjas) [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat-square&logoColor=white&link=https://www.youtube.com/@thiago_tjas)](https://www.youtube.com/@thiago_tjas) [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logoColor=white&link=https://www.instagram.com/thiago.tjas/)](https://www.instagram.com/thiago.tjas/) [![Website](https://img.shields.io/badge/-Website-888888?style=flat-square&logoColor=white&link=http://thiago-tjas.com/)](http://thiago-tjas.com/) [![GitHub](https://img.shields.io/badge/-GitHub-555555?style=flat-square&logoColor=white&link=https://github.com/tjas)](https://github.com/tjas)

## Licence

* Code distributed under [MIT License](https://github.com/tjas/tjas-erp/blob/master/LICENCE).
