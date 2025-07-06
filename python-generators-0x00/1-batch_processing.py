#!/usr/bin/python3

import MySQLdb


def stream_users_in_batches(batch_size):
    """
    Generator function that fetches rows in batches from the user_data table.
    
    Args:
        batch_size (int): Number of rows to fetch in each batch
        
    Yields:
        list: A batch of rows from the database
    """
    try:
        # Connect to the ALX_prodev database
        connection = MySQLdb.connect(
            host="localhost",
            user="prodev",
            passwd="avellin",
            db="ALX_prodev",
            port=3306,
            charset='utf8'
        )
        
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user_data")
        
        # Fetch rows in batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
        cursor.close()
        connection.close()
        
    except MySQLdb.Error as e:
        print(f"Database error: {e}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return


def batch_processing(batch_size):
    """
    Processes batches of users and filters those over the age of 25.
    
    Args:
        batch_size (int): Number of rows to fetch in each batch
    """
    # Use the stream_users_in_batches generator to get batches
    for batch in stream_users_in_batches(batch_size):
        # Filter users over age 25 in the current batch
        for user in batch:
            if user['age'] > 25:
                print(user)
