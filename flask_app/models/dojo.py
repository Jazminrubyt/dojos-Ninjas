from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:
    _db = "dojo_ninja_db"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def retrieve_info(cls):
        """retrieve all dojos info from database"""
        query = "Select * FROM dojos;"
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query)
        print("************")
        pprint(list_of_dicts)
        print("************")

        dojos = []
        for dojo_info in list_of_dicts:
            dojo = Dojo(dojo_info)
            dojos.append(dojo)
        return dojos

    @classmethod
    def retrieve_by_id_with_ninjas(cls, dojo_id):
        """Finds one dojo by id and related ninja"""

        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = (%(dojo_id)s);
        """
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query, data)
        pprint(list_of_dicts)
        dojo = Dojo(list_of_dicts[0])
        print(dojo.name)
        for each_dict in list_of_dicts:
            if each_dict["ninjas.id"] != None:

                ninja_data = {
                    "id": each_dict["ninjas.id"],
                    "first_name": each_dict["first_name"],
                    "last_name": each_dict["last_name"],
                    "age": each_dict["age"],
                    "dojo_id": each_dict["dojo_id"],
                    "created_at": each_dict["ninjas.created_at"],
                    "updated_at": each_dict["ninjas.updated_at"],
                }
                ninja = Ninja(ninja_data)
                dojo.ninjas.append(ninja)
        return dojo

    @classmethod
    def create(cls, form_data):
        """insert a new dojo into the database"""
        query = """
        INSERT INTO dojos
        (name)
        Values
        (%(name)s);
        """
        dojo_id = connectToMySQL(Dojo._db).query_db(query, form_data)
        return dojo_id

    @classmethod
    def retrieve_info_id(cls, dojo_id):
        """retrieve one dojo info from database"""
        query = "SELECT * FROM dojos WHERE id = (%(dojo_id)s);"
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL(Dojo._db).query_db(query, data)
        pprint(list_of_dicts)
        return Dojo(list_of_dicts[0])

    @classmethod
    def update(cls, form_data):
        """Update a dojo by id"""

        query = """
        UPDATE dojos
        SET
        name = %(name)s,
        WHERE id = %(dojo_id)s;
        """
        connectToMySQL(Dojo._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, dojo_id):
        """Deletes a user by id"""

        query = "DELETE FROM dojos WHERE id = %(dojo_id)s;"
        data = {"dojo_id": dojo_id}
        connectToMySQL(Dojo._db).query_db(query, data)
        return
