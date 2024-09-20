#pip install pymongo
from pymongo import MongoClient
connetion = MongoClient() # mongod 인스턴스 생성

# print(connetion)
# DB 생성
db = connetion["Test"]
# print(db)

# 컬렉션 생성
collection = db.AAA
# print(collection)

# create
post = {"name" : "user1",
        "Timeline" : "I sometimes cry",
        "follow" : "200"}

# db.컬렉션명.insertOne(document)
# x = collection.insert_one(post)
# print(x)

# insert_many() : 여러 문서 추가, 리스트에 여러 딕셔너리
post = [{"name" : "user2",
        "Timeline" : "I sometimes A",
        "follow" : 0},
        {"name" : "user3",
        "Timeline" : "I sometimes B",
        "follow" : 200},
        {"name" : "user4",
        "Timeline" : "I sometimes C",
        "follow" : 1}]
# x = collection.insert_many(post)
# print(x)

# CRUD : Read 조회
# find_one() : 가장 빨리 검색되는 문서 하나 검색, 조건 입력 가능
# x = collection.find_one()
# print(x)
# x = collection.find_one({"name":"user2"})
# print(x)

# find() 문서 전체 검색
docs = collection.find()
for doc in docs:
    print(doc)

# 원하는 필드만 조회 : 두번째 인수로 원하는 필드를 넣어준다.
# name, Timeline, 조회:1 조회안함:0
# _id는 기본이 항상 조회되는 1이므로 0이라고 명시를 하여야 한다.
# docs = collection.find({},{'_id':0, 'name':1, 'Timeline':1})
# for doc in docs:
#     print(doc)

# follow를 기준으로 내림차순 정렬
# 정렬 : -1은 내림차순, 1은 오름차순
# docs = collection.find().sort({'follow':-1})
# for doc in docs:
#     print(doc)

# 조건 추가 follw수가 1이상인 다큐먼트의 name과 follow
# 조건은 첫번째 인수에 가입한다
# 연산자 사용 $gt(초과) $gte(이상) $lt(미만) $lte(이하) $ne(같지않음) $or(또는) $in(배열요소중 하나)

# docs = collection.find({ '$expr': { '$gt': [{'$toInt':'$follow'},1] }},{'_id':0, 'name':1, 'Timeline':1, 'follow':1})
# for doc in docs:
#     print(doc)

# document 문서의 수
docs = collection.count_documents({})
print(docs)

# update(수정)
# name이 user2인 follow의 수를 80으로 수정하시오
# 첫번째 객체(인수)에 수정할 다큐먼트 지정, 두번째 인수에는 수정할 내용을 입력한다.
# x = collection.update_one({'name':'user2'},{'$set':{'follow':'100'}})
# x = collection.update_many({'name':'user2'},{'$set':{'follow':'100'}})
# print(x)

# user2인 회원 찾아서 프린트하시오
# docs = collection.find({"name":"user2"})
# for doc in docs:
#   print(doc)

# post = {"name" : "user2",
#         "Timeline" : "I sometimes cry",
#         "follow" : 0}
# collection.insert_one(post)

# 삭제 delete
# x = collection.delete_one({'name':'user2'})
# x = collection.delete_many({'name':'user2'})
# print(x)
# xs = collection.find()
# for x in xs:
#     print(x)


