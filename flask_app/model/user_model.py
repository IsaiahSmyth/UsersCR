from flask_app.config.mysqlconnection import connectToMySQL


class User:
    DB = "user_db"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO user (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update_user(cls, data):
        query = """UPDATE user SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, created_at = %(created_at)s
        WHERE id = %(id)s ;"""

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM user WHERE id = %(id)s;"""

        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0]) 
    # Make an object out of the first dictionary in the list of Results.


    @classmethod
    def delete_user(cls, data):
        query = """DELETE FROM user WHERE id = %(id)s ; """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result