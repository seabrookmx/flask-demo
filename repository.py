from sqlite3 import dbapi2 as sqlite3


class Repository:
    db = None

    def __init__(self, db_path):
        self.db = self.get_db(db_path)

    @staticmethod
    def get_db(db_path: str):
        sqlite_db = sqlite3.connect(db_path)
        sqlite_db.row_factory = sqlite3.Row
        return sqlite_db

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.dispose()

    def dispose(self):
        self.db.close()

    def init_db(self, bootstrap_str: str):
        # Execute a random string against the DB
        # ONLY USE THIS TO INITIALIZE THE DB
        self.db.cursor().executescript(bootstrap_str)
        self.db.commit()

    @staticmethod
    def parse_entry(entry: list) -> object:
        return {
            'id': entry[0],
            'title': entry[1],
            'text': entry[2]
        }

    def list_entries(self, keyword: str) -> object:
        entries = None

        query_string = 'select id, title, text from entries'
        if keyword is not None:
            query_string += ' where title like ? order by id desc;'
            like_clause = '%' + keyword + '%'

            # second parameter to execute is a sequence so we have to have the weird (thing,) syntax
            entries = self.db.execute(query_string, (like_clause,)).fetchall()
        else:
            query_string += ' order by id desc;'
            entries = self.db.execute(query_string).fetchall()

        object_result = []
        for entry in entries:
            object_result.append(self.parse_entry(entry))

        return object_result

    def get_entry(self, id: str) -> object:
        query_string = 'select id, title, text from entries where id = ?'
        entries = self.db.execute(query_string, [id]).fetchall()

        if len(entries) < 1:
            return None

        return entries[0]
