#!/usr/bin/env python3
import mysql.connector
import csv
import os
from mysql.connector import Error

DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"

def connect_db():
    """Connects to the MySQL server"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # adjust to your password if needed
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    """Creates the ALX_prodev database if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
    except Error as e:
        print(f"Database creation error: {e}")

def connect_to_prodev():
    """Connects to the ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # adjust to your password if needed
            database=DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error connecting to {DB_NAME}: {e}")
        return None

def create_table(connection):
    """Creates the user_data table if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Table creation error: {e}")

def insert_data(connection, csv_filename):
    """Inserts data into the user_data table from a CSV file"""
    try:
        cursor = connection.cursor()
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute(f"""
                    SELECT * FROM {TABLE_NAME} WHERE user_id = %s
                """, (row['user_id'],))
                if cursor.fetchone():
                    continue
                cursor.execute(f"""
                    INSERT INTO {TABLE_NAME} (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (row['user_id'], row['name'], row['email'], row['age']))
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Data insertion error: {e}")
    except FileNotFoundError:
        print(f"CSV file '{csv_filename}' not found.")
