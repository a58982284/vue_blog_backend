import json
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['hearthstone']
collection=db['cards']

with open('./cards.json',encoding='utf-8') as f:
    try:
        while True:
            line = f.readline()
            if line:
                r = json.loads(line)
                print(len(r))
                # result = collection.insert_many(r)
            else:
                break
    except:
        f.close()