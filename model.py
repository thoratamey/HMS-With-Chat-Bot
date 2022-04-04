#Python 2.7

import sqlite3
import json
import pyodbc

server = 'tcp:hmsdatabase.database.windows.net'
database = 'hmsdatabase'
username = 'hmsdatabase'
password = 'Hms@database'
driver = '{ODBC Driver 18 for SQL Server}'

conn = pyodbc.connect('DRIVER=' + driver +
                      ';SERVER=' + server +
                      ';DATABASE=' + database +
                      ';UID=' + username +
                      ';PWD=' + password)

conn = conn.cursor()




def dict_factory(cursor, row):
    """This is an function use to fonmat the json when retirve from the  myswl database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




conn.execute('''CREATE TABLE patient
(pat_id INT IDENTITY(1,1) NOT NULL,
pat_first_name TEXT NOT NULL,
pat_last_name TEXT NOT NULL,
pat_insurance_no TEXT NOT NULL,
pat_ph_no TEXT NOT NULL,
pat_date DATE DEFAULT CURRENT_TIMESTAMP,
pat_address TEXT NOT NULL,
PRIMARY KEY (pat_id));''')

conn.execute('''CREATE TABLE doctor
(doc_id INT IDENTITY(1,1) NOT NULL,
doc_first_name TEXT NOT NULL,
doc_last_name TEXT NOT NULL,
doc_ph_no TEXT NOT NULL,
doc_date DATE DEFAULT CURRENT_TIMESTAMP,
doc_address TEXT NOT NULL,
PRIMARY KEY (doc_id));''')

conn.execute('''CREATE TABLE appointment
(app_id INT IDENTITY(1,1) NOT NULL,
pat_id INTEGER NOT NULL,
doc_id INTEGER NOT NULL,
appointment_date DATE NOT NULL,
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id));''')