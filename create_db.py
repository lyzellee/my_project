import os
from sqlalchemy.engine.url import make_url
import mysql.connector 
from mysql.connector import Error
from config import Config 

def create_database_if_not_exist():
    try:
        url =make_url(Config.SQLALCHEMY_DATABASE_URI)
        if url.get_backend_name() != 'mysql':
            print("Only mysql is supported by this script")
            return False
        user = url.username or ""
        password = url.password or ""
        host = url.host or ""
        port = url.port or 3306
        database = url.database

        if not database:
            print("No database name in SQLALCHEMY URI")
            return False
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        cur = conn.cursor()
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database}`"
            f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        print ("Database `{database}` is ready")
        cur.close(); conn.close()
        return True 
    except Error as e:
        print(f"Mysql error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    
if __name__ == "__main__":
    ok = create_database_if_not_exist()
    print("Done" if ok else "Failed.")