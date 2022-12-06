# habits
# Habit Tracker

This app will allow users to create their own list of Habits and mark them done daily.

> This project was built as a part ot [PythonToProject Bootcamp](https://bhavaniravi.gumroad.com/l/LaFSj)

## Feature list
USER LOGIN
NEW USER REGISTER
CREATE A HABIT
LIST HABITS
LOG HABITS DAILY
UPDATE HABIT
DELETE HABIT


## Architecture/Flow Diagram



## API Design

List all the APIs it's methods, request and response params

1.CREATE HABIT - POST - HABIT - /create_habit
2.LIST ALL HABITS - GET - HABIT - /log_habit
3.MARK HABIT - POST - HABIT - /mark_habit
4.DELETE HABIT - DELETE - HABIT - /habitika/<item_id>
5.LIST Habit by ID - GET - HABIT - /habitika/<item_id>
6.LOGIN USER
7.REGISTER NEW USER
8.LOGOUT



## DB Design Diagram

> TABLE 1- HABIT
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
>  TABLE 2 - USER
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email EMAIL NOT NULL,
            Password PASSWORD NOT NULL,
            CreatedOn Date DEFAULT CURRENT_DATE                        



## Coding Issues and Learning
