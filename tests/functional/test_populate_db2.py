# pylint: disable=R0801
"""
     Testy tworzenia bazy danych oraz populacji danych do utworzonej bazy
"""

import unittest
from os import getenv
from tests.test_db_abstract import TestDbAbstractTestCase

db_name = getenv('DB_DB_NAME')
db_user = getenv('DB_DB_USER')
db_pass = getenv('DB_DB_PASS')
db_host = getenv('DB_DB_HOST')
db_port = getenv('DB_DB_PORT')
URL = f'ibm_db_sa://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


class DB2DBTestCase(TestDbAbstractTestCase):
    """Testing class"""

    def test_all(self):
        """ Testing all remade functions in DB2 """

        self.func_create_schema(URL)
        self.func_endpoint_users(URL)
        self.func_endpoint_posts(URL)
        self.func_endpoint_comments(URL)
        self.func_endpoint_albums(URL)
        self.func_endpoint_photos(URL)
        self.func_endpoint_todos(URL)


if __name__ == '__main__':
    unittest.main()
