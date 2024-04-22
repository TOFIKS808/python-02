## Local development with `venv`
* run `make venv` to create `venv`
* run `. ./venv/bin/activate` to activate `venv`
* run `make pip` to install dependencies
* run `make lint` to lint code
* run `make test` to run tests

## Development in Docker
* run `make up`
* open in browser http://127.0.0.1:81 for Jupyter Notebook
* run `make d-pip` to install dependencies in container
* run `make d-lint` to lint code in container
* run `make d-test` to run tests in container


https://medium.com/@arthurapp98/using-sqlalchemy-to-create-and-populate-a-postgresql-database-with-excel-data-eb6049d93402

## Description

Program that implements handling the population of the database with API data into multiple systems which are:
    - Postgres
    - mariadb
    - oracle
    - Ms SQL
    - IBM DB2
    - SQLite

