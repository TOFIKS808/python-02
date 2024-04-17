# pylint: disable=R0801
"""
     Test populacji danych do Modelu
"""

import unittest
from os import getenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import requests
from src.Model import Base, User, Company, Address, Geo


class ModelPopulateTestCase(unittest.TestCase):
    """
         Test populacji danych do Modelu
    """

    def setUp(self):
        self.db_name = getenv('DB_NAME_TEST')
        self.db_user = getenv('DB_USER')
        self.db_pass = getenv('DB_PASS')
        self.db_host = getenv('DB_HOST')
        self.db_port = getenv('DB_PORT')

    def test_model(self):
        """
             Test bazy danych
        """

        engine = create_engine(
            f"postgresql+psycopg2://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
        )

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        result = requests.get("https://jsonplaceholder.typicode.com/users", timeout=2)

        data = []
        for user in result.json():
            obj_user = User(
                id=user['id'],
                name=user['name'],
                username=user['username'],
                email=user['email'],
                phone=user['phone'],
                website=user['website'],
                company=Company(
                    name=user["company"]["name"],
                    catch_phrase=user["company"]["catchPhrase"],
                    bs=user["company"]["bs"]
                ),
                address=Address(
                    street=user["address"]["street"],
                    suite=user["address"]["suite"],
                    city=user["address"]["city"],
                    zipcode=user["address"]["zipcode"],
                    geo=Geo(
                        lat=user["address"]["geo"]["lat"],
                        long=user["address"]["geo"]["lng"]
                    )
                ),
            )
            data.append(obj_user)
        with Session(engine) as session:
            for obj in data:
                session.add(obj)

            session.commit()

        with Session(engine) as session:

            db_user_1: User = session.execute(select(User).where(User.id == 1)).scalars().first()
            self.assertEqual(1, db_user_1.id)
            self.assertEqual("Leanne Graham", db_user_1.name)
            self.assertEqual("Bret", db_user_1.username)
            self.assertEqual("Sincere@april.biz", db_user_1.email)
            self.assertEqual("1-770-736-8031 x56442", db_user_1.phone)
            self.assertEqual("hildegard.org", db_user_1.website)


if __name__ == '__main__':
    unittest.main()
