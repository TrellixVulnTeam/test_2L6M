from elasticsearch import Elasticsearch, helpers, NotFoundError
import time
from time import sleep

es = Elasticsearch("http://localhost:9200")

def putIndexTemplate():
    body = {
        "index_patterns": "*",
        "template": {
            "settings": {
                "number_of_shards": 1
            }
        }
    }
    es.indices.put_index_template("template_test_1", body)

def getIndexTemplate():
    result = es.indices.get_index_template("template_test_1")
    print(result)

def deleteIndices():
    es.indices.delete(index='students*', request_timeout=3600)

def getIndices():
    result = es.indices.get(index='students*')
    print(len(result))

def generateData(idx):
    for i in range(5):
        if i % 2 == 0:
            idx_name = ("shio-index" + str(i))
        else:
            idx_name = ("tani-index" + str(i))
        yield {
            "_op_type": "create",
            "_index": idx_name,
            "_source": {
                "name": ("Jiro" + str(i)),
                "age": (25 + i),
                "email": "jiro{}@example.com".format(str(i))
            }
        }

def bulk():
    for idx in range(1):
        helpers.bulk(es, generateData(idx))

def checkIndex():
    idx = "students100,students101,students1,students2,students3,students4,students700,students709"
    start_time = time.time()
    result = es.indices.get(index=idx, ignore_unavailable=True)
    # sleep(2)
    end_time = time.time()
    print("{} 秒".format(end_time - start_time))
    print(len(result.keys()))

def search():
    indices = ""
    for idx in range(10):
        indices += ("students" + str(idx) + ",")
    result = es.search(index=indices, ignore_unavailable=True, size=10000)
    for r in result["hits"]["hits"]:
        print(r)

#putIndexTemplate()
#getIndexTemplate()
#getIndices()
#bulk()
#checkIndex()
#search()
#deleteIndices()
