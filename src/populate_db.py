"""

"""
from os import getenv
import requests as rq
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, drop_database, create_database

from Model import Base, User, Company, Address, Geo

db_name = getenv('DB_NAME')
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


def create_db() -> None:
    """create new db, drop if exists"""
    engine = create_engine(URL)
    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)


def create_schema() -> None:
    """create tables"""
    engine = create_engine(URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def endpoint_users() -> None:
    result = rq.get("https://jsonplaceholder.typicode.com/users", timeout=2)
    engine = create_engine(URL)
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


if __name__ == '__main__':
    """populate db"""
    create_db()
    create_schema()
    endpoint_users()
