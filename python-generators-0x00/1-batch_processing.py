import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches of `batch_size`"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Processes each batch, filters users over age 25, and returns the list"""
    filtered_users = []
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                filtered_users.append(user)

    return filtered_users
