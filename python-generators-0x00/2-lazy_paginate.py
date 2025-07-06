#!/usr/bin/python3

seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Fetches a specific page of users from the database.
    
    Args:
        page_size (int): Number of rows to fetch per page
        offset (int): Number of rows to skip
        
    Returns:
        list: A list of user records from the database
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    
    # Get column names for MySQLdb
    column_names = [desc[0] for desc in cursor.description]
    
    # Convert tuples to dictionaries
    result = []
    for row in rows:
        result.append(dict(zip(column_names, row)))
    
    connection.close()
    return result


def lazy_pagination(page_size):
    """
    Generator function that lazily loads pages of users from the database.
    Only fetches the next page when needed.
    
    Args:
        page_size (int): Number of rows to fetch per page
        
    Yields:
        list: A page of user records from the database
    """
    offset = 0
    
    while True:
        # Fetch the next page using the paginate_users function
        page = paginate_users(page_size, offset)
        
        # If no more records, stop iteration
        if not page:
            break
            
        # Yield the current page
        yield page
        
        # Move to the next page
        offset += page_size
