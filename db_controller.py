import sqlite3
connection = sqlite3.connect("company.db") ## CREATE DATABASE company;
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = 1")
