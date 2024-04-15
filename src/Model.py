"""
    Budowa bazy danych
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    """ Base class """
    pass


class User(Base):
    """ budowa tabeli users """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(30))
    website: Mapped[str] = mapped_column(String(30))
    company: Mapped["Company"] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, name={self.name!r}, fullname={self.username!r}, fullname={self.email!r}, "
                f"fullname={self.phone!r}, fullname={self.website!r})")


class Company(Base):
    """ budowa tabeli company """
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="company")
    name: Mapped[str] = mapped_column(String(50))
    catch_phrase: Mapped[str] = mapped_column(String(30))
    bs: Mapped[str] = mapped_column(String(30))


class Address(Base):
    """ budowa tabeli address """
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    street: Mapped[str] = mapped_column(String(50))
    suite: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(30))
    zipcode: Mapped[str] = mapped_column(String(30))


class Geo(Base):
    """ budowa tabeli geo """
    __tablename__ = "geo"
    id: Mapped[int] = mapped_column(primary_key=True)
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
    lat: Mapped[str] = mapped_column(String(50))
    long: Mapped[str] = mapped_column(String(30))
