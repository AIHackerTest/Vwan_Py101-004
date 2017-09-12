import sqlite3
import os

def setup(db_name, table_name):
    # root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # db_name = os.path.join(root_dir, 'resource', 'my_weather.db')
    print(db_name)
    conn = connect_db(db_name)
    create_table(conn, table_name)  # to move to other places later
    conn.commit()
    return conn

def connect_db(db_name):
    conn = sqlite3.connect(db_name, check_same_thread=False)
    return conn

def create_table(conn, table_name):
    # cur.execute("drop table if exists " + db_name)
    conn.cursor().execute(f"""create table if not exists {table_name}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                city Text,
                date Text,
                weather Text,
                wind Text,
                temperature Text,
                last_updated_on Text)""")

def insert_(record):
    keys = "'" + "','".join(record.keys()) + "'"
    values = "'" +  "','".join(record.values()) + "'"
    print(keys)
    print(values)
    print(f"""insert into {table_weather}
                ({keys}) values ({values})""")
    cur.execute(f"""insert into weather_info
                ({keys}) values ({values})""")

def update_(record):
    cur.execute(f"""update {table_weather}
                set {record.key} = {record.value})""")

def search_():
    cur.execute(f"select * from {table_weather}")

def count_():
    cur.execute(f"select count(*) from {table_weather}")

def commit_():
    conn.commit()

def close_():
    conn.commit()
    conn.close()
