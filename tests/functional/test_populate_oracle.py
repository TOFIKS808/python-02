"""
     Testy tworzenia bazy danych oraz populacji danych do utworzonej bazy
"""
import unittest
from os import getenv
from tests.test_db_abstract import TestDbAbstractTestCase

db_name = getenv('O_DB_NAME')
db_user = getenv('O_DB_USER')
db_pass = getenv('O_DB_PASS')
db_host = getenv('O_DB_HOST')
db_port = getenv('O_DB_PORT')


URL = f'oracle+cx_oracle://{db_user}:{db_pass}@{db_host}:{db_port}/?service_name={db_name}'


class OracleTestCase(TestDbAbstractTestCase):
    """ Testing class """
    def test_all(self):
        """ Testing all remade functions in Postgres """
        # self.func_create_db(URL)
        self.func_create_schema(URL)
        self.func_endpoint_users(URL)
        self.func_endpoint_posts(URL)
        self.func_endpoint_comments(URL)
        self.func_endpoint_albums(URL)
        self.func_endpoint_photos(URL)
        self.func_endpoint_todos(URL)


if __name__ == '__main__':
    unittest.main()
