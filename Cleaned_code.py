from loguru import logger
import mysql.connector
from encrypt_decrypt import decrypt

def read_from_mysql(config, query):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=config['mysql_database']['host'],
            user=config['mysql_database']['user'],
            password=decrypt(config['mysql_database']['password']),
            database=config['mysql_database']['database']
        )

        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info(result)
        return result

    except Exception as e:
        logger.error(f"Error occurred in MySQL DB: {e}")
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
