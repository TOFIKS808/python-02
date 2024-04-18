"""
    Potulating db with SQLite
"""
import unittest
import os
from tests.test_db_abstract import TestDbAbstractTestCase


class SQLiteTestCase(TestDbAbstractTestCase):
    """Testing class"""

    def test_all(self):
        """ Testing all remade functions in SQLite """
        folder = './var'
        if not os.path.exists(folder):
            os.makedirs(folder)

        db_file = f'{folder}/test.db'
        if os.path.exists(db_file):
            os.remove(db_file)

        url = f'sqlite:///{db_file}'

        self.func_create_db(url)
        self.func_create_schema(url)
        self.func_endpoint_users(url)
        self.func_endpoint_posts(url)
        self.func_endpoint_comments(url)
        self.func_endpoint_albums(url)
        self.func_endpoint_photos(url)
        self.func_endpoint_todos(url)


if __name__ == '__main__':
    unittest.main()
