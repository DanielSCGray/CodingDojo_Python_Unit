from mysql_connection import connect_to_mysql

DATABASE = 'sql_flask_users'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        # insert a new row representing a new user
        query = '''
        insert into users (first_name, last_name, email)
        values (%(first_name)s, %(last_name)s, %(email)s);
        '''
        user_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return user_id
    
    @classmethod
    def get_all(cls):
        query = 'select * from users'
        results = connect_to_mysql(DATABASE).query_db(query)
        users = []
        for dict in results:
            users.append(User(dict))
        return users
        
    @classmethod
    def get_one(cls, user_id):
        query = '''
        select * from users 
        where id = %(user_id)s;
        '''
        data = {'user_id': user_id}
        result = connect_to_mysql(DATABASE).query_db(query, data)
        user = User(result[0])
        return user
    
    @classmethod
    def update(cls, form_data):
        query = '''
        update users
        set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        where id = %(user_id)s;
        '''

        connect_to_mysql(DATABASE).query_db(query, form_data)
        return
    
    @classmethod
    def delete(cls, user_id):
        query = '''
        delete from users where id = %(user_id)s;
        '''
        data = {'user_id': user_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return

