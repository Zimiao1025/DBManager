import sqlite3
from pymongo import MongoClient

# 连接SQLite数据库
conn = sqlite3.connect('/data/protein/CAMEO/database/cameo.db')
cursor = conn.cursor()

# 从SQLite数据库读取数据
cursor.execute('SELECT * FROM state_tbl')
rows = cursor.fetchall()

# 连接MongoDB
client = MongoClient('mongodb://localhost:27017/')

db = client['casp15']
collection = db['cameo']

# 将数据导入MongoDB
for row in rows:
    print("Name: ", row[1])
    data = {
        'hash_id': row[0],
        'name': row[1],
        'sender': row[2],
        'receive_time': row[3],
        'request_json': row[4],
        'state': row[5],
        'state_msg': row[6],
        'event_time_json': row[7],
        'path_tree': row[8],
        'plddt': row[9],
        'lddt': row[10],
        'reserved': row[11],
        'error': row[12],
        'visible': row[13]
    }
    collection.insert_one(data)

# 关闭连接
conn.close()
client.close()
