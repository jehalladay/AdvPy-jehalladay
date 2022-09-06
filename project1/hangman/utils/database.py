'''
    Assignment - Project 1: Hangman
    File: database.py
    Description: This program will control the database used in the hangman game
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022


    *******************************************************************************

    *******************************************************************************
'''

import sqlite3

def connect_to_db(db_name: str) -> sqlite3.Connection:
    '''
    This function will connect to the database
    '''
    return sqlite3.connect(db_name)

def create_table(conn: sqlite3.Connection, table_name: str, columns: list, schema: list) -> None:
    '''
    This function will create a table
    '''
    cursor = conn.cursor()
    cols = [' '.join(i) for i in zip(columns, schema)]
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(cols)})'
    print(cols, query)
    cursor.execute(query)
    conn.commit()

def insert_into_table(conn: sqlite3.Connection, table_name: str, columns: list, values: list) -> None:
    '''
    This function will insert a record into a table
    '''
    cursor = conn.cursor()
    # values = [f'"{i}"' for i in values]
    place_holders = ['?' for i in range(len(values))]
    query = f'INSERT INTO {table_name} ({",".join(columns)}) VALUES ({",".join(place_holders)})'
    print(columns, values, query)
    cursor.execute(query, values)
    conn.commit()

def check_for_record(conn: sqlite3.Connection, table_name: str, column: str, value: str) -> bool:
    '''
    This function will check for a record in a table
    '''
    cursor = conn.cursor()
    query = f'SELECT * FROM {table_name} WHERE {column} = ?'
    cursor.execute(query, (value,))
    return None != cursor.fetchone()

def delete_record(conn: sqlite3.Connection, table_name: str, column: str, value: str) -> None:
    '''
        This function will delete a record from a table
    '''

    cursor = conn.cursor()
    query = f'DELETE FROM {table_name} WHERE {column} = ?'
    cursor.execute(query, (value,))
    conn.commit()

