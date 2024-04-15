"""
     Test bazy danych
"""

import unittest
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.Model import Base, User, Company


class MyTestCase(unittest.TestCase):
    """
         Test bazy danych
    """
    def setUp(self):
        self.db_name = getenv('DB_NAME')
        self.db_user = getenv('DB_USER')
        self.db_pass = getenv('DB_PASS')
        self.db_host = getenv('DB_HOST')
        self.db_port = getenv('DB_PORT')

    def test_something(self):
        """
             Test bazy danych
        """

        engine = create_engine(
            f"postgresql+psycopg2://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
        )

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        bruce = User(
            name="Bruce Lee",
            username="bruce",
            email="bruce@lee.com",
            phone="123213123",
            website="www.lee.com",
            company=Company(name="XXX", catch_phrase="xxxxxxx", bs="bull shit"),
            # address='',
        )
        with Session(engine) as session:
            # for z danymi z api
            session.add(bruce)
            # session.add_all([bruce])


            session.commit()



if __name__ == '__main__':
    unittest.main()
