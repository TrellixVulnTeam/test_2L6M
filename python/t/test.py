from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
result = es.search(index="students0,students2,students5,students8,students10", ignore_unavailable=True, size=10000)
for r in result["hits"]["hits"]:
        print(r)
