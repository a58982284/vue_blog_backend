import json
import pymongo
import time
import uuid

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['myblog']
collection=db['article']

# with open('./cards.json',encoding='utf-8') as f:
#     try:
#         while True:
#             line = f.readline()
#             if line:
#                 r = json.loads(line)
#                 print(len(r))
#                 # result = collection.insert_many(r)
#             else:
#                 break
#     except:
#         f.close()

article = {
"articleId": str(uuid.uuid1()).replace('-', ''),
  "title": '日本最漫长的一天',
  "tag": '历史',
  "describtion": '日本终战日',
  "createDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,
  "content": "日本投降是指1945年8月15日大日本帝国宣布向同盟国无条件投降，且于同年9月2日举行投降仪式并正式签署降书的历史事件。1945年7月大日本帝国海军实际上已无法继续执行作战任务，同时同盟国也不断对日本实施包括东京大轰炸在内的空袭行动、并开始策划入侵日本本土的没落行动。虽然以军事参议官会议为首的日本政府公开表示仍打算继续坚持与同盟国作战，然而日本高层也开始私下拜托保持中立国立场的苏联就和平一事进行谈判，期望能尽可能争取日本和平投降后仍处于有利的谈判地位。但与此同时苏联则依据其在德黑兰会议和雅尔塔会议中与美国及英国所做的承诺，开始准备计划攻击日本于海外布署的部队。"
}

result = collection.insert_one(article)
print(result)