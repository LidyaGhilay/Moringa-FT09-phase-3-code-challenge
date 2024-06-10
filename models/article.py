from database.connection import get_db_connection


class Article:
    def __init__(self, title=None, content=None, author=None):
        self.title = title
        self.content = content
        self.author = author




class Author:
    def __init__(self, name): 
        self._name = name
        self._id = None

        if name is not None:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()

    @property
    def id(self):
        if self._id is not None:
            return self._id
        else:
            return -1  

    @property
    def name(self):
        if self._name is not None:
            return self._name
        else:
            return "Unknown"  

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("the name should be a string")
        self._name = value

    def articles(self):
        return "trial"

    def magazines(self):
        return "trial"


# models/magazine.py
class Magazine:
    def __init__(self, id=None, name=None):
        if id is None and name is None:
            raise ValueError(" provide the id or name")

        self._id = id if id is not None else -1
        self.name = name if name is not None else "Unnamed"

    