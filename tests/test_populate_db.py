# pylint: disable=R0801
"""
     Testy tworzenia bazy danych oraz populacji danych do utworzonej bazy
"""

import unittest
from os import getenv
import sqlalchemy as sql
from sqlalchemy import orm
from sqlalchemy_utils import database_exists
from src.populate_db import create_db, create_schema, endpoint_users, endpoint_posts, endpoint_comments, \
    endpoint_albums, endpoint_photos, endpoint_todos
from src.Model import User, Post, Comment, Album, Photo, Todo

db_name = getenv('DB_NAME_TEST')
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


class PopulateDbTestCase(unittest.TestCase):
    """Testing class"""

    def test_populate(self):
        """ Functions Handler """
        self.func_create_db()
        self.func_create_schema()
        self.func_endpoint_users()
        self.func_endpoint_posts()

    def func_create_db(self):
        """Database creation test"""
        create_db(URL)
        engine = sql.create_engine(URL)
        self.assertTrue(database_exists(engine.url))

    def func_create_schema(self):
        """ Tables creation test """
        create_schema(URL)
        engine = sql.create_engine(URL)
        self.assertTrue(sql.inspect(engine).has_table('address'))
        self.assertTrue(sql.inspect(engine).has_table('album'))
        self.assertTrue(sql.inspect(engine).has_table('comment'))
        self.assertTrue(sql.inspect(engine).has_table('company'))
        self.assertTrue(sql.inspect(engine).has_table('geo'))
        self.assertTrue(sql.inspect(engine).has_table('photo'))
        self.assertTrue(sql.inspect(engine).has_table('post'))
        self.assertTrue(sql.inspect(engine).has_table('todo'))
        self.assertTrue(sql.inspect(engine).has_table('users'))

    def func_endpoint_users(self):
        """ Populating users table test """

        endpoint_users(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            users = session.execute(sql.select(User)).scalars().all()
            self.assertEqual(10, len(users))
            user: User = users[1]
            self.assertIsInstance(user, User)
            self.assertEqual(2, user.id)
            self.assertEqual("Ervin Howell", user.name)
            self.assertEqual("Antonette", user.username)
            self.assertEqual("Shanna@melissa.tv", user.email)
            self.assertEqual("Victor Plains", user.address.street)
            self.assertEqual("Suite 879", user.address.suite)
            self.assertEqual("Wisokyburgh", user.address.city)
            self.assertEqual("90566-7771", user.address.zipcode)
            self.assertEqual("-43.9509", user.address.geo.lat)
            self.assertEqual("-34.4618", user.address.geo.long)

    def func_endpoint_posts(self):
        """ Populating post table test """

        endpoint_posts(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            posts = session.execute(sql.select(Post)).scalars().all()
            self.assertEqual(100, len(posts))
            post: Post = posts[1]
            self.assertEqual(1, post.user_id)
            self.assertEqual(2, post.id)
            self.assertEqual("qui est esse", post.title)
            self.assertEqual(post.body,
                             "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores"
                             " neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam"
                             " non debitis possimus qui neque nisi nulla")

    def func_endpoint_comments(self):
        """ Populating comment table test """

        endpoint_comments(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            comments = session.execute(sql.select(Comment)).scalars().all()
            self.assertEqual(500, len(comments))
            comment: Comment = comments[1]
            self.assertEqual(1, comment.post_id)
            self.assertEqual(2, comment.id)
            self.assertEqual("quo vero reiciendis velit similique earum", comment.name)
            self.assertEqual("Jayne_Kuhic@sydney.com", comment.email)
            self.assertEqual(comment.body, "est natus enim nihil est dolore omnis voluptatem numquam\net omnis"
                                           " occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint"
                                           " nostrum voluptatem reiciendis et")

    def func_endpoint_albums(self):
        """ Populating album table test """

        endpoint_albums(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            albums = session.execute(sql.select(Album)).scalars().all()
            self.assertEqual(100, len(albums))
            album: Album = albums[1]
            self.assertEqual(1, album.user_id)
            self.assertEqual(2, album.id)
            self.assertEqual(album.title, "sunt qui excepturi placeat culpa")

    def func_endpoint_photos(self):
        """ Populating photo table test """

        endpoint_photos(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            photos = session.execute(sql.select(Photo)).scalars().all()
            self.assertEqual(5000, len(photos))
            photo: Photo = photos[1]
            self.assertEqual(1, photo.album_id)
            self.assertEqual(2, photo.id)
            self.assertEqual(photo.title, "eprehenderit est deserunt velit ipsam")
            self.assertEqual(photo.url, "https://via.placeholder.com/600/771796")
            self.assertEqual(photo.thumbnail_url, "https://via.placeholder.com/150/771796")

    def func_endpoint_todos(self):
        """ Populating todo table test """

        endpoint_todos(URL)
        engine = sql.create_engine(URL)
        with orm.Session(engine) as session:
            todos = session.execute(sql.select(Todo)).scalars().all()
            self.assertEqual(5000, len(todos))
            todo: Todo = todos[1]
            self.assertEqual(1, todo.user_id)
            self.assertEqual(2, todo.id)
            self.assertEqual(todo.title, "quis ut nam facilis et officia qui")
            self.assertEqual(todo.completed, False)


if __name__ == '__main__':
    unittest.main()
