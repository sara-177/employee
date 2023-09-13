# # 1, Import libraries:
import mysql.connector
from mysql.connector import Error
#
#
# # __________________________________________
#
#
# 2. Connects to the MySQL database server:
def create_connection(host_name, user_name, user_password, unix_socket,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            unix_socket=unix_socket,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "root", "/Applications/MAMP/tmp/mysql/mysql.sock","em_app")

#
# # __________________________________________
#

# # 3. Create the database:
# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# create_database_query = "CREATE DATABASE em_app"
# create_database(connection, create_database_query)

#
# # __________________________________________
#
#
# # 4. Create function to excute queries:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# # __________________________________________
#

# 5. Create queries for creating tables:
# # #
# create_employees_table = """
# create_employees_table = """
# CREATE TABLE employees (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# ) ENGINE = InnoDB
# """
#
# create_position_table = """
  # CREATE TABLE IF NOT EXISTS position (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   salary INTEGER
 # ) ENGINE = InnoDB

# # """
#
# create_department_table = """
# CREATE TABLE IF NOT EXISTS department (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   description TEXT
# ) ENGINE = InnoDB
# """
# #
# # # # #
# create_emplposition_table = """
# CREATE TABLE IF NOT EXISTS emplposition (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   position_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (position_id) REFERENCES position (id)
# )  ENGINE=InnoDB;
# """
# # # #
# create_empldepartment_table = """
# CREATE TABLE IF NOT EXISTS empldepartment (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   dep_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (dep_id) REFERENCES department (id)
# ) ENGINE = InnoDB
# """
# # #
# create_emplrate_table = """
# CREATE TABLE IF NOT EXISTS emplrate (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   rate INTEGER,
#   FOREIGN KEY (emply_id) REFERENCES employees (id)
#   ) ENGINE = InnoDB
# """
# execute_query(connection, create_employees_table)
# execute_query(connection, create_position_table)
# # execute_query(connection, create_department_table)
# execute_query(connection, create_emplposition_table)
# execute_query(connection, create_empldepartment_table)
# execute_query(connection, create_emplrate_table)

# # # # __________________________________________
# #
# #
# # # 6. Create INSERT queries:
# #
# create_employees = """
# INSERT INTO
#   employees (name, age, gender, nationality)
# VALUES
#   ('abdullah', 34, 'male', 'jeddah'),
#   ('leila', 32, 'female', 'riyadh'),
#   ('sara', 30, 'female', 'French');
# # """
# #
# create_position = """
# INSERT INTO
#   position (name, salary)
# VALUES
#   ('marketing', 7200),
#   ('Human Resources Representative', 9100),
#   ('programmer', 5000);
# """
#
# create_department = """
# INSERT INTO
#   department (name, description)
# VALUES
#   ('Administration', 'finance, public relations and marketing'),
#    ('HR', 'Human Resources'),
#    ('IT','information technology');
#
#
# """
#
# create_emplposition = """
# INSERT INTO
#   emplposition (emply_id, position_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (3, 3);
# """

# create_empldepartment = """
# INSERT INTO
#   empldepartment (emply_id, dep_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (3, 3);
# """

#
# create_emplrate = """
# INSERT INTO
#   emplrate (emply_id, dep_id)
# VALUES
#   (1, 4),
#   (2, 5),
#   (3, 3);
# """
# execute_query(connection, create_employees)
# execute_query(connection, create_position)
# execute_query(connection, create_department)
# execute_query(connection, create_emplposition)
# execute_query(connection, create_empldepartment)
# execute_query(connection, create_emplrate)




# # __________________________________________
#
#
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
# __________________________________________
#
#
# # 7. Create SELECT queries:
# select_employees = "SELECT * FROM employees"
# employees = execute_read_query(connection, select_employees)
#
# for employee in employees:
#     print(employee)

#
# select_employees_department = """
# SELECT
#   employees.id,
#   employees.name,
#     department.name
#
# FROM
#   department
#    inner JOIN employees ON employee.id = department.emply_id
# """
# employees = execute_read_query(connection, select_employees_department)
#
# for employee in employees:
#     print(employee)
# """
#----------------------------------------------

# # 8. Create SELECT queries with WHERE:
# #
# # select_employees = """
#
# select * from employees where name = 'sara';
#
# """
# employees = execute_read_query(connection, select_employees)
# for employee in employees:
#     print(employee)
# # __________________________________________
#
#
# 9. Create Update queries:
# update_department_description = """
# UPDATE
#   department
# SET
#   description = " finance"
# WHERE
#   id = 1
# """
#
# execute_query(connection,  update_department_description)
#
#
# # __________________________________________
#
#
# # # 10. Create Delete queries:
# delete_employee = "DELETE FROM employees WHERE id = 2"
# execute_query(connection, delete_employee)

