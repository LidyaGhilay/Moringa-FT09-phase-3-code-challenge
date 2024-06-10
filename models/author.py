from database.connection import get_db_connection

class Author:
    def __init__(self, name=None):
        self._id = None
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Invalid")
        if not isinstance(value, str):
            raise TypeError("The author name must be a string")
        if len(value) == 0:
            raise ValueError("The author name cannot be empty")
        if hasattr(self, '_name'):
            raise AttributeError("The author's name cant be changed after instantiation")
        self._name = value

    def save(self):
        if hasattr(self, '_id'):
            raise AttributeError("The author is in the database")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO authors (name) VALUES (?);
        ''', (self.name,))
        conn.commit()
        conn.close()


   