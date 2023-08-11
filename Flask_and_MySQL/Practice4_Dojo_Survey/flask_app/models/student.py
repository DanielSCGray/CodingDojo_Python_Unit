from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash

DATABASE = 'dojo_survey_schema'

class Student:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_info(data):
        is_valid = True
        if len(data['name']) < 1:
            is_valid = False
            flash('Name is required')
        if data['location'] == 'None':
            is_valid = False
            flash('Please select a location')
        if data['language'] == 'None':
            is_valid = False
            flash('Please select a language')
        return is_valid

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO students (name, location, language, comment)
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)'''
        student_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return student_id
    
    @classmethod 
    def get_all(cls):
        query = 'SELECT * FROM students'
        result = connect_to_mysql(DATABASE).query_db(query)
        students = []
        for student in result:
            students.append(Student(student))
        return students