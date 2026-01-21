logger.info(result)from src.main.databases.mysql_connector_clean_code import read_from_mysql
from loguru import logger
import configparser

def main():
    config = configparser.ConfigParser()
    config.read(
        r"C:\Users\hp\Desktop\Data Engineering Python\src\resources\config_file.ini"
    )

    query = "SELECT * FROM labours_table"
    final_result = read_from_mysql(config, query)
    logger.info(final_result)

if __name__ == "__main__":
    main()
