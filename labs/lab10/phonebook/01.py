import psycopg2
import csv

conn = psycopg2.connect(database = "postgres",
                        host = 'localhost',
                        user = "postgres",
                        password = "dana3262")


csv_file = "csv_file.csv"


def create_table():

    command = """CREATE TABLE phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                phone_number VARCHAR(20) UNIQUE
            )"""

    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()


def insert_users_from_csv(csv_file_name):
    command = """INSERT INTO phonebook(name, phone_number) VALUES(%s, %s)"""

    with conn.cursor() as cur:
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            #_ = next(csvreader)
            for row in csvreader:
                name, phone = row
                cur.execute(command, (name, phone))
        conn.commit()

def insert_users_from_console():

    command = """INSERT INTO phonebook(name, phone_number) VALUES(%s, %s)"""

    name = input("name: ")
    phone = input("number: ")

    with conn.cursor() as cur:
        cur.execute(command, (name, phone))
        conn.commit()


def updating_name(new_value, old_value):
    command = """UPDATE phonebook SET name = %s WHERE name = %s"""

    with conn.cursor() as cur:
        cur.execute(command, (new_value, old_value))
        conn.commit()

def query_data(filter = None):
    command = f"SELECT * FROM phonebook {filter}"

    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)


def delete_data(column, value):
    command = f"DELETE FROM phonebook WHERE {column} = %s"

    with conn.cursor() as cur:
        cur.execute(command, (value,))
        conn.commit()


#create_table()
#insert_users_from_console()
#insert_users_from_csv(csv_file)
#query_data("WHERE name = 'Dana'")
#updating_name("Hello", "AAAA")
delete_data("name", "Hello")
query_data()


conn.close()
