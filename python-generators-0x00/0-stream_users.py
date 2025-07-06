#!/usr/bin/python3

import MySQLdb


def stream_users():
    """
    Generator function that fetches rows one by one from the user_data table.
    Uses yield to return each row as it's fetched from the database.
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
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        
        # Fetch and yield rows one by one
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
            
        cursor.close()
        connection.close()
        
    except MySQLdb.Error as e:
        print(f"Database error: {e}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return


# Make the module callable by creating a class that implements __call__
class StreamUsersModule:
    def __call__(self):
        return stream_users()

# Replace the current module with an instance of our callable class
import sys
sys.modules[__name__] = StreamUsersModule()
