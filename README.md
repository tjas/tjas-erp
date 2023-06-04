# tjas-erp

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](./README.md)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Ftjas-erp&count_bg=%2379C83D&title_bg=%23555555&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Stars](https://img.shields.io/github/stars/tjas/tjas-erp?color=yellow)](https://github.com/tjas/tjas-erp)
[![Watchers](https://badgen.net/github/watchers/tjas/tjas-erp/)](https://github.com/tjas/tjas-erp/watchers)
[![Python](https://img.shields.io/badge/python-v3.10.11-darkgreen)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-v4.2.1-green)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-v15.3.0-blue)](https://www.postgresql.org/)

> ⭐ Mark the project with a star.

> 👀 Watch the project for receive news.

> 🌐 Access my personal website: [thiago-tjas.com](http://thiago-tjas.com/)

> 🇧🇷 Acesse a versão em [Português do Brasil](./README_pt-br.md).

Advanced Python/Django ERP application for product, employee and sales registration, detailing, editing, deletion and listing, with access control. Features and evolutions planned can be found in the *Features and Todo List* section.

## Build With

* Python 3.10.11
* Django 4.2.1
* PostgreSQL 15.3.0

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
6. Make sure [PostgreSQL](https://www.postgresql.org/) is running on your computer and that the ```db_erp``` database has been created. The database access and other related settings must be verified and can be changed in the ```DATABASES``` variable of ```settings.py``` file, located in main application folder (```core``` module).
7. Run the migrations
    ```py
    python manage.py migrate
    ```
8. Run Django project
    ```py
    python manage.py runserver
    ```
9. Then access aplication at http://127.0.0.1:8000/

## Contributing

> Adapted from the ["Flappy Bird: Dev Soutinho"](https://github.com/omariosouto/flappy-bird-devsoutinho/blob/master/CONTRIBUTING.md) project.

1. Fork it!
2. Create your feature branch:
```
git checkout -b my-new-feature
```
3. Add files changed:
```
git add .
```
4. Commit your changes:
```
git commit -m "Add some feature"
```
5. Push to the branch:
```
git push origin my-new-feature
```
6. Submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    - Add a title and description that let clear your suggestion.
    - After your pull request is merged, you can safely delete your branch.

## Features and Todo List
 
- [x] Create employees' registration, detailing, editing and listing;
- [x] Create products' registration, detailing, editing, deletion and listing;
- [x] Create sales' registration, detailing, editing, deletion and listing;
- [x] Create public and private pages access control;
- [x] Create connection to persist informations in local data base;
- [ ] Create rich user interface with [Bootstrap](https://getbootstrap.com/);
- [ ] Create new product, employee and sale's fields and categories;
- [ ] Create products' stock control;
- [ ] Create stores' registration, detailing, editing, deletion and listing;
- [ ] Create link between stores and employees;
- [ ] Create stores' public and restrict access pages;
- [ ] Create customers' registration, detailing, editing and listing;
- [ ] Create customers' rich shopping page;
- [ ] Create customers' shopping cart;
- [ ] Create customers' following store list;
- [ ] Create customers' favorites list;
- [ ] Create customers' purchase history page;
- [ ] Create customers' shipping address page;
- [ ] Create customers' payment method page;
- [ ] Create purchase steps with payment method and delivery address;
- [ ] Create pagination in listing views;
- [ ] Create filters in listing views;
- [ ] Create translation to other languages.

## Contact

* **Thiago Jorge Almeida dos Santos**: Project author and maintainer ⁘ [LinkedIn](https://www.linkedin.com/in/thiago-tjas) ⁘ [YouTube](https://www.youtube.com/@thiago_tjas) ⁘ [Instagram](https://www.instagram.com/thiago.tjas/) ⁘ [GitHub](https://github.com/tjas)

* Project Link: https://github.com/tjas/tjas-erp

## Licence

* © 2023 Thiago Jorge Almeida dos Santos, all rights reserved.
