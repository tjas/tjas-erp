# tjas-erp

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](./README.md)
[![Acessos](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Ftjas-erp&count_bg=%2379C83D&title_bg=%23555555&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Stars](https://img.shields.io/github/stars/tjas/tjas-erp?color=yellow)](https://github.com/tjas/tjas-erp)
[![Watchers](https://badgen.net/github/watchers/tjas/tjas-erp/)](https://github.com/tjas/tjas-erp/watchers)
[![Python](https://img.shields.io/badge/python-v3.10.11-darkgreen)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-v4.2.1-green)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-v15.3.0-blue)](https://www.postgresql.org/)

> ⭐ Marque o projeto com uma estrela (clique em "Star").

> 👀 Acompanhe o projeto (clique em "Watch") para receber novidades.

> 🌐 Acesse meu site pessoal: [thiago-tjas.com](http://thiago-tjas.com/)

> 🇺🇸 Access the [US English](./README.md) version.

Aplicação ERP Python/Django avançada para cadastro, detalhamento, edição, exclusão e listagem de produtos, funcionários e vendas, com controle de acesso. As funcionalidades e evoluções previstas podem ser encontradas na seção *Funcionalidades e lista de tarefas a serem realizadas*.

## Principais tecnologias utilizadas

* Python 3.10.11
* Django 4.2.1
* PostgreSQL 15.3.0

## Utilização

Este é um exemplo de como você pode configurar o projeto localmente no seu computador. Recomendamos fortemente que você utilize um ambiente virtual para rodar a aplicação, recomendamos a utilização do [Virtualenv](https://virtualenv.pypa.io/en/latest/) (ou qualquer outro de sua preferência). Leia, crie e ative o ambiente virtual dentro da pasta do projeto antes do passo 5.

Para obter uma cópia local funcionando, siga estas etapas:

1. Certifique-se de que você tem o Python 3.10.11+ instalado ou verifique como fazê-lo em [Python.org](https://www.python.org/) ou por meio do [Anaconda](https://www.anaconda.com/);
2. Certifique-se de que você tem o Git instalado ou verifique como fazê-lo em [Git-scm.com](https://git-scm.com/);
3. Acesse a pasta na qual você deseja salvar o projeto, então, clone o repositório nesta pasta
```sh
git clone https://github.com/tjas/tjas-erp
```
4. Acesse a pasta do projeto;
5. Instale as dependências do projeto
   ```py
   pip install -r requirements.txt
   ```
6. Certifique-se de que o [PostgreSQL](https://www.postgresql.org/) está rodando em sua máquina e que o banco de dados ```db_erp``` foi criado. Os dados de acesso ao banco de dados e demais configurações devem ser verificados e podem ser alterados na variável ```DATABASES``` do arquivo ```settings.py```, localizado na pasta principal (módulo ```core```) da aplicação.
7. Execute as *migrations*
    ```py
    python manage.py migrate
    ```
8. Execute o projeto Django
    ```py
    python manage.py runserver
    ```
9. Finalmente, acesse a aplicação no endereço: http://127.0.0.1:8000/

## Contribuição

> Adaptado do projeto ["Flappy Bird: Dev Soutinho"](https://github.com/omariosouto/flappy-bird-devsoutinho/blob/master/CONTRIBUTING.md).

1. Crie um fork!
2. Crie sua feature branch:
```
git checkout -b my-new-feature
```
3. Adicione os arquivos modificados:
```
git add .
```
4. Faça um Commit com suas alterações:
```
git commit -m "Add some feature"
```
5. Faça um push da sua branch:
```
git push origin my-new-feature
```
6. Envie um [Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) para esse repositório
    - Adicione um título e uma descrição que deixe claro sua sugestão.
    - Depois que seu pull request for mergeado, você pode apagar sua branch.

## Funcionalidades e lista de tarefas a serem realizadas

- [x] Criar cadastro, detalhamento, edição e listagem de funcionários;
- [x] Criar cadastro, detalhamento, edição, exclusão e listagem de produtos;
- [x] Criar cadastro, detalhamento, edição, exclusão e listagem de vendas;
- [x] Criar controle de acesso de páginas públicas e privadas;
- [x] Criar conexão para persistência de informações em base de dados local;
- [ ] Criar interface de usuário mais avançada com [Bootstrap](https://getbootstrap.com/);
- [ ] Criar novos campos e categorias de produtos, funcionários e vendas;
- [ ] Criar controle de estoque de produtos;
- [ ] Criar cadastro, detalhamento, edição, exclusão e listagem de lojas;
- [ ] Criar vinculação entre lojas e funcionários;
- [ ] Criar páginas de acesso público e restrito das lojas;
- [ ] Criar cadastro, detalhamento, edição, exclusão e listagem de clientes;
- [ ] Criar uma página de compras avançada para os clientes;
- [ ] Criar carrinho de compras de clientes;
- [ ] Criar listas de lojas seguidas por clientes;
- [ ] Criar listas de favoritos de clientes;
- [ ] Criar página de histórico de compras de clientes;
- [ ] Criar página de endereços de entrega do cliente;
- [ ] Criar página de métodos de pagamento do cliente;
- [ ] Criar etapas de compra com forma de pagamento e endereço de entrega;
- [ ] Criar paginação nas visões de listagem;
- [ ] Criar filtros nas visões de listagem;
- [ ] Criar tradução para outros idiomas.

## Contact

* **Thiago Jorge Almeida dos Santos**: autor e mantenedor do projeto ⁘ [LinkedIn](https://www.linkedin.com/in/thiago-tjas) ⁘ [YouTube](https://www.youtube.com/@thiago_tjas) ⁘ [Instagram](https://www.instagram.com/thiago.tjas/) ⁘ [GitHub](https://github.com/tjas)

* Link para o projeto: https://github.com/tjas/tjas-erp

## Licence

* © 2023 Thiago Jorge Almeida dos Santos, todos os direitos reservados.
