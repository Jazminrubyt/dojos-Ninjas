from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Ninja:
    _db = "dojo_ninja_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def retrieve_info(cls):
        """retrieve all users info from database"""
        query = "Select * FROM ninjas;"
        list_of_dicts = connectToMySQL(Ninja._db).query_db(query)
        pprint(list_of_dicts)

        ninjas = []
        for ninja_info in list_of_dicts:
            ninja = Ninja(ninja_info)
            ninjas.append(ninja)
        return ninjas

    @classmethod
    def create(cls, form_data):
        """insert a new user into the database"""
        query = """
        INSERT INTO ninjas
        (first_name, last_name, age, dojo_id)
        Values
        (%(first_name)s,  %(last_name)s, %(age)s, %(dojo_id)s);
        """
        ninja_id = connectToMySQL(Ninja._db).query_db(query, form_data)
        return ninja_id

    @classmethod
    def retrieve_info_id(cls, ninja_id):
        """retrieve one user info from database"""
        query = "SELECT * FROM ninjas WHERE id = (%(ninja_id)s);"
        data = {"ninja_id": ninja_id}
        list_of_dicts = connectToMySQL(Ninja._db).query_db(query, data)
        pprint(list_of_dicts)
        return Ninja(list_of_dicts[0])

    @classmethod
    def update(cls, form_data):
        """Update a ninja by id"""

        query = """
        UPDATE ninjas
        SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        age = %(age)s
        WHERE id = %(ninja_id)s;

        """
        connectToMySQL(Ninja._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, ninja_id):
        """Deletes a ninja by id"""

        query = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
        data = {"ninja_id": ninja_id}
        connectToMySQL(Ninja._db).query_db(query, data)
        return
