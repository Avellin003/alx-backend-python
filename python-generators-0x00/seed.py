#!/usr/bin/python3

import MySQLdb
import csv
import uuid


def connect_db():
    """Connects to the MySQL database server"""
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="prodev",
            passwd="avellin",
            port=3306,
            charset='utf8'
        )
        return connection
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        return None


def create_database(connection):
    """Creates the database ALX_prodev if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
        print("Database ALX_prodev created or already exists")
    except MySQLdb.Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL"""
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="prodev",
            passwd="avellin",
            db="ALX_prodev",
            port=3306,
            charset='utf8'
        )
        return connection
    except MySQLdb.Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    """Creates a table user_data if it does not exist with the required fields"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(250) NOT NULL,
            email VARCHAR(250) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """)
        connection.commit()
        cursor.close()
        print("Table user_data created or already exists")
    except MySQLdb.Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_filename):
    """Inserts data in the database if it does not exist"""
    try:
        # Read and insert data from CSV file
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            cursor = connection.cursor()
            
            for row in csv_reader:
                # Check if data already exists based on name and email combination
                check_query = "SELECT COUNT(*) FROM user_data WHERE name = %s AND email = %s"
                cursor.execute(check_query, (row['name'], row['email']))
                result = cursor.fetchone()
                
                if result[0] == 0:  # Data doesn't exist, insert it
                    # Generate UUID for user_id
                    user_id = str(uuid.uuid4())
                    
                    insert_query = """
                    INSERT INTO user_data (user_id, name, email, age) 
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (user_id, row['name'], row['email'], row['age']))
                    connection.commit()
                    print(f"Inserted: {row['name']}")
                else:
                    print(f"Data already exists for: {row['name']}")
            
            cursor.close()
            print(f"Data insertion from {csv_filename} completed")
            
    except FileNotFoundError:
        print(f"CSV file {csv_filename} not found")
    except MySQLdb.Error as e:
        print(f"Error inserting data: {e}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")


def main():
    """Main function to execute the database setup and data population"""
    # Step 1: Connect to MySQL server
    server_connection = connect_db()
    if not server_connection:
        return
    
    # Step 2: Create database
    create_database(server_connection)
    server_connection.close()
    
    # Step 3: Connect to ALX_prodev database
    db_connection = connect_to_prodev()
    if not db_connection:
        return
    
    # Step 4: Create table
    create_table(db_connection)
    
    # Step 5: Insert data from CSV
    insert_data(db_connection, 'user_data.csv')
    
    # Close connection
    db_connection.close()
    print("Database setup and data population completed")


if __name__ == "__main__":
    main()