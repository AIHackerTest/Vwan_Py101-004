import sqlite3
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
db_name = os.path.join(root_dir, 'resource', 'my_weather.db')
print(db_name)

conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute('drop table if exists weather_info')
cur.execute("""create table if not exists weather_info
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            city Text,
            date Text,
            weather Text,
            wind Text,
            temperature Text,
            last_updated_on Text)""")
cur.execute("""insert into weather_info
            (city, date, weather, wind, temperature, last_updated_on)
            values ('beijing', '2017-9-9', '清', '微风', 27, '2019-9-9')""")
conn.commit()
cur.execute('select * from weather_info')
print(cur.fetchall())
conn.close()
