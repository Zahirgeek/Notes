from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

# 连接服务器
conn = MongoClient("47.106.138.135", 27017)
# 连接数据库
db = conn.axf
# 获取集合
collection = db.student

# 查询所有
# res = collection.find()
# print(res)
# print(type(res))
# for stu in res:
#     print(stu)

# 查询部分
# res = collection.find({"age": {"$gt": 40}})
# for stu in res:
#     print(stu)

# 统计查询
# print(collection.find({"age":{"$gt":40}}).count())


#排序
# res = collection.find().sort("age", pymongo.DESCENDING)
# for stu in res:
#     print(stu)


# 分页相关
# res = collection.find().limit(5)
# for stu in res:
#     print(stu)



# _id查询
print(collection.find_one({"_id":ObjectId('5b865c3b8ad03c4c28e530ee')}))




#断开链接
conn.close()
