from flask_app.config.mysql_connection import connect_to_mysql

# Set DATABASE below

DATABASE = ''

#overwrite all instances of 'example' with the table name

class Example:
    def __init__(self, data):
        self.id = data['id']
        #fill property in as needed, ctrl d 4 times to update create method aswell
        self.property1 = data['property1']
        self.property2 = data['property2']
        self.property3 = data['property3']
        self.property4 = data['property4']
        self.parent_id = data['parent_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        #delete excess props, remember parent/one in the relation's ID must be inserted by form aswell
        query = '''
        INSERT INTO examples (property1, property2, property3, property4, parent_id)
        VALUES (%(property1)s, %(property2)s, %(property3)s, %(property4)s, %(parent_id)s );
        '''
        example_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return example_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM examples;'
        result = connect_to_mysql(DATABASE).query_db(query)
        examples = []
        for example in result:
            examples.append(Example(example))
        return examples
    
    @classmethod
    def get_by_id(cls, example_id):
        query = 'SELECT * FROM examples WHERE id = %(example_id)s;'
        data = {'example_id': example_id}
        result = connect_to_mysql(DATABASE).query_db(query, data)
        example = Example(result[0])
        return example
    
    @classmethod
    def update(cls, form_data):
        #Remember the edit form should use a hidden input to provide the id of the example data being edited
        query = '''UPDATE examples
        SET properety1=%(properety1)s, property2=%(property2)s, property3=%(property3)s, property4=%(property4)s, property5=%(property5)s
        WHERE id = %(example_id)s;'''
        return connect_to_mysql(DATABASE).query_db(query, form_data)

    @classmethod
    def delete(cls, example_id):
        query = '''
        delete from examples where id = %(example_id)s;
        '''
        data = {'example_id': example_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return