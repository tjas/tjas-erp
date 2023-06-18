# tjas-erp

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg?label=Status)](./README.md)
[![Acessos](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Ftjas-erp&count_bg=%2379C83D&title_bg=%23555555&title=Acessos&edge_flat=false)](https://hits.seeyoufarm.com)
![Cobertura de testes](https://img.shields.io/badge/coverage-76%25-yellow?label=Cobertura%20de%20testes)
[![Licença](https://img.shields.io/github/license/tjas/tjas-erp?color=orange&label=Licença)](https://github.com/tjas/tjas-erp/blob/master/LICENCE)
[![Commits](https://img.shields.io/github/commit-activity/t/tjas/tjas-erp?label=Commits)](https://github.com/tjas/tjas-erp/graphs/commit-activity)
![Último commit](https://img.shields.io/github/last-commit/tjas/tjas-erp?color=blue&label=Último%20commit)
![Tamanho do repositório](https://img.shields.io/github/repo-size/tjas/tjas-erp?color=888888&label=Tam.%20repositório)
![Tamanho do código](https://img.shields.io/github/languages/code-size/tjas/tjas-erp?color=888888&label=Tam.%20código)
[![Stars](https://img.shields.io/github/stars/tjas/tjas-erp?color=blue&label=Stars)](https://github.com/tjas/tjas-erp)
[![Watchers](https://img.shields.io/github/watchers/tjas/tjas-erp?color=blue&label=Watchers)](https://github.com/tjas/tjas-erp/watchers)
[![Forks](https://img.shields.io/github/forks/tjas/tjas-erp?color=blue&label=Forks)](https://github.com/tjas/tjas-erp/forks)

[![Python](https://img.shields.io/badge/python-v3.10.11-darkgreen?label=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-v4.2.1-green?label=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-v15.3.0-blue?label=PostgreSQL)](https://www.postgresql.org/)

> ⭐ Marque o projeto com uma estrela. 👀 Acompanhe o projeto para receber novidades.
>
> 🇺🇸 Access this page in [US English](./README.md).
<!-- >
> 🌐 Acesse meu site pessoal: [thiago-tjas.com](http://thiago-tjas.com/) -->

Aplicação ERP Python/Django avançada para cadastro, detalhamento, edição, exclusão e listagem de produtos, funcionários e vendas, com controle de acesso. As funcionalidades e evoluções previstas podem ser encontradas na seção [Principais Funcionalidades Disponíveis](#principais-funcionalidades-disponíveis).

<!-- 
## Principais tecnologias utilizadas

* Python 3.10.11
* Django 4.2.1
* PostgreSQL 15.3.0 
-->

## Principais Funcionalidades Disponíveis

> Para saber mais sobre lançamentos futuros, acesse o [Planejamento de Lançamentos](https://github.com/users/tjas/projects/2/views/1)

* Cadastro, detalhamento, edição e listagem de funcionários;
* Cadastro, detalhamento, edição, exclusão e listagem de produtos;
* Cadastro, detalhamento, edição, exclusão e listagem de vendas;
* Controle de acesso de páginas públicas e privadas;
* Conexão para persistência de informações em base de dados local;
* 76% de cobertura de testes.

<!-- 
* Criar interface de usuário mais avançada com [Bootstrap](https://getbootstrap.com/);
* Criar novos campos e categorias de produtos, funcionários e vendas;
* Criar controle de estoque de produtos;
* Criar cadastro, detalhamento, edição, exclusão e listagem de lojas;
* Criar vinculação entre lojas e funcionários;
* Criar páginas de acesso público e restrito das lojas;
* Criar cadastro, detalhamento, edição, exclusão e listagem de clientes;
* Criar uma página de compras avançada para os clientes;
* Criar carrinho de compras de clientes;
* Criar listas de lojas seguidas por clientes;
* Criar listas de favoritos de clientes;
* Criar página de histórico de compras de clientes;
* Criar página de endereços de entrega do cliente;
* Criar página de métodos de pagamento do cliente;
* Criar etapas de compra com forma de pagamento e endereço de entrega;
* Criar paginação nas visões de listagem;
* Criar filtros nas visões de listagem;
* Criar tradução para outros idiomas.
-->

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
6. Certifique-se de que o [PostgreSQL](https://www.postgresql.org/) está rodando em sua máquina e que o banco de dados ```db_erp``` foi criado. O nome, os dados de acesso ao banco de dados e demais configurações devem ser verificadas e podem ser alteradas na variável ```DATABASES``` do arquivo ```settings.py```, localizado na pasta principal (módulo ```core```) da aplicação.
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
<!-- > Adaptado do projeto ["Flappy Bird: Dev Soutinho"](https://github.com/omariosouto/flappy-bird-devsoutinho/blob/master/CONTRIBUTING.md). -->

1. Crie um fork!
2. Crie sua branch de funcionalidade:
    ```sh
    git checkout -b minha-nova-funcionalidade
    ```
3. Adicione os arquivos modificados:
    ```sh
    git add .
    ```
4. Faça um Commit com suas alterações:
    ```sh
    git commit -m "Adicione algum comentário útil aqui"
    ```
5. Faça um push da sua branch:
    ```sh
    git push origin minha-nova-funcionalidade
    ```
6. Envie um [Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) para esse repositório
    * Adicione um título e uma descrição que deixe claro sua sugestão;
    * Utilize o idioma inglês para comentários e nomes de branch;
    * Depois que seu pull request for mergeado, você pode apagar sua branch.

## Testes

Para a criação de testes unitários foram utilizadas, principalmente, as ferramentas disponíveis no módulo [```django.test```](https://docs.djangoproject.com/pt-br/4.2/topics/testing/) do Django e na biblioteca [unittest](https://docs.python.org/3/library/unittest.html) do Python. Para aferir a cobertura de testes foi utilizado o pacote [coverage](https://pypi.org/project/coverage/).

### Realização de testes

De dentro da pasta do projeto execute:

```sh
python manage.py test
```

### Verificação da cobertura de testes

De dentro da pasta do projeto execute a ferramenta e gere relatórios:

```sh
coverage run --omit='*/venv/*' manage.py test
coverage report
coverage html
```

## Contato

**Thiago Jorge Almeida dos Santos**, autor e mantenedor do projeto.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logoColor=white&link=https://www.linkedin.com/in/thiago-tjas)](https://www.linkedin.com/in/thiago-tjas) [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat-square&logoColor=white&link=https://www.youtube.com/@thiago_tjas)](https://www.youtube.com/@thiago_tjas) [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logoColor=white&link=https://www.instagram.com/thiago.tjas/)](https://www.instagram.com/thiago.tjas/) [![Website](https://img.shields.io/badge/-Website-888888?style=flat-square&logoColor=white&link=http://thiago-tjas.com/)](http://thiago-tjas.com/) [![GitHub](https://img.shields.io/badge/-GitHub-555555?style=flat-square&logoColor=white&link=https://github.com/tjas)](https://github.com/tjas)

## Licença

* Código distribuído sob a [Licença MIT](https://github.com/tjas/tjas-erp/blob/master/LICENCE).
