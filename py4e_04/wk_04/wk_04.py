#produce an SQLite database that contains a User, Course, and Member table
#and populate the tables from the data file.

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member
    ''')

cur.executescript('''
    CREATE TABLE User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    );

    CREATE TABLE Course(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT
    );

    CREATE TABLE Member(
    course_id INTEGER,
    user_id INTEGER,
    role INTEGER,
    PRIMARY KEY(course_id, user_id)
    )
    ''')

file = open('roster_data.json').read()
data = json.loads(file) #parse the json file

for entry in data:
    #read through each entry of the data, and get name, title, and role
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]


    cur.execute('INSERT OR IGNORE INTO User(name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT INTO Member(course_id,user_id,role)
        VALUES (?,?,?)''',(course_id,user_id,role))

conn.commit()
