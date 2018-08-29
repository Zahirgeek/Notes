from pymongo import MongoClient

# 连接服务器
conn = MongoClient("47.106.138.135", 27017)
# 连接数据库
db = conn.axf
# 获取集合
collection = db.student

collection.remove({"name": "lilei"})

# 断开连接
conn.close()

