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

test_find_all=collection.find()

structure ={}
for test_find_one in test_find_all:
    print(test_find_one)
    break

# 关闭连接
conn.close()
client.close()
