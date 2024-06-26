# pylint: disable=R0801
"""
     Testy tworzenia bazy danych oraz populacji danych do utworzonej bazy
"""
import unittest
from os import getenv
from tests.test_db_abstract import TestDbAbstractTestCase

db_name = getenv('MS_DB_NAME')
db_user = getenv('MS_DB_USER')
db_pass = getenv('MS_DB_PASS')
db_host = getenv('MS_DB_HOST')
db_port = getenv('MS_DB_PORT')


URL = f'mssql+pymssql://{db_user}:{db_pass}@{db_host}/{db_name}'


class MicrosoftTestCase(TestDbAbstractTestCase):
    """ Testing class """
    def test_all(self):
        """ Testing all remade functions in MSSQL """
        self.func_create_db(URL)
        self.func_create_schema(URL)
        self.func_endpoint_users(URL)
        self.func_endpoint_posts(URL)
        self.func_endpoint_comments(URL)
        self.func_endpoint_albums(URL)
        self.func_endpoint_photos(URL)
        self.func_endpoint_todos(URL)


if __name__ == '__main__':
    unittest.main()
