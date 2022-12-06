import sqlite3
import random
from datetime import datetime


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('habittracker.db')
        self.create_user_table()
        self.create_habit_table()

    def create_habit_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Habit" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email EMAIL NOT NULL,
            Password PASSWORD NOT NULL,
            CreatedOn Date DEFAULT CURRENT_DATE)     
        """

        self.conn.execute(query)


class User_Model:
    TABLENAME = "USER"

    def __init__(self):
        self.conn = sqlite3.connect('habittracker.db')

    def create_user(self, params):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Username, Password) ' \
                f'values ("{params["Name"]}","{params["Username"]}","{params["Password"]}")'

        result = self.conn.execute(query)
        self.conn.commit()
        return result

    def check_user(self, username, password):
        searchquery = f'SELECT * from {self.TABLENAME} where Username = "{username}" and Password = "{password}"'
        cursor = self.conn.cursor()
        cursor.execute(searchquery)
        info = cursor.fetchone()
        return info


class Habit_Model:
    TABLENAME = "HABIT"

    def __init__(self):
        self.conn = sqlite3.connect('habittracker.db')

    def create_habit(self, params):

        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description, DueDate, _is_done, is_deleted, UserId) ' \
                f'values ("{params["Title"]}","{params["Description"]}", NULL, false, false,"{params["UserId"]}")'

        result = self.conn.execute(query).rowcount
        self.conn.commit()
        return result


    def list_habit(self, user_id):

        searchquery = f"SELECT id, Title, Description from {self.TABLENAME} " \
                      f"where is_deleted = {0} and _is_done = {0} and DueDate IS NOT CURRENT_DATE and UserId = {user_id}"

        cursor = self.conn.cursor()
        cursor.execute(searchquery)
        result_set = cursor.fetchall()

        for item in result_set:
            print(item)

        return result_set

    def get_by_id(self, search_id):
        searchquery = f"SELECT id, Title, Description, DueDate, _is_done, is_deleted from {self.TABLENAME} where id = " + search_id
        result_set = self.conn.execute(searchquery).fetchall()
        return result_set

    def update_habit(self, user_id, params):
        update_query = f'UPDATE {self.TABLENAME} ' \
                       f'SET _is_done = "{params["is_done"]}", ' \
                       f'DueDate = CURRENT_DATE ' \
                       f'WHERE id = {params["id"]} AND ' \
                       f'UserId = {user_id}'

        update_obj = self.conn.execute(update_query)
        self.conn.commit()
        return update_obj


    def delete(self, item_id):
        delete_query = f'UPDATE {self.TABLENAME} ' \
                       f'SET is_deleted = "{1}" ' \
                       f'WHERE id = {item_id}'

        self.conn.execute(delete_query)
        self.conn.commit()
        return self.get_by_id(item_id)
