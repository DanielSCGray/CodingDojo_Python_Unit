from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import user
from flask import flash

DATABASE = 'recipes_db'

#overwrite all instances of 'example' with the table name

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        #fill property in as needed
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.creator_id = data['creator_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'].strip()) < 3:
            is_valid = False 
            flash('Name must be 3+ characters')
        if len(data['description'].strip()) < 3:
            is_valid = False 
            flash('Descripton must be 3+ characters')
        if len(data['instructions'].strip()) < 3:
            is_valid = False 
            flash('Instructions must be 3+ characters')
        
        if data['date_made'] == '':
            is_valid = False
            flash('Date made is required')

        if 'under_30' not in data.keys():
            is_valid = False
            flash('Under 30 minutes is required')
        return is_valid

    @classmethod
    def create(cls, form_data):
        #fill data fields as needed
        query = '''
        INSERT INTO recipes (name, description, instructions, under_30, date_made, creator_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date_made)s, %(creator_id)s);
        '''
        recipe_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return recipe_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes;'
        result = connect_to_mysql(DATABASE).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(Recipe(recipe))
        return recipes
    
    @classmethod
    def get_by_id(cls, recipe_id):
        query = 'SELECT * FROM recipes WHERE id = %(recipe_id)s;'
        data = {'recipe_id': recipe_id}
        result = connect_to_mysql(DATABASE).query_db(query, data)
        recipe = Recipe(result[0])
        return recipe
    
    @classmethod
    def update(cls, form_data):
        query = '''UPDATE recipes
        SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s
        WHERE id = %(recipe_id)s;'''
        return connect_to_mysql(DATABASE).query_db(query, form_data)
    
    @classmethod
    def delete(cls, recipe_id):
        query = '''
        delete from recipes where id = %(recipe_id)s;
        '''
        data = {'recipe_id': recipe_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
