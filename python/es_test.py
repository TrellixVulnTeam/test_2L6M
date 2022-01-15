from operator import index
from elasticsearch import Elasticsearch, helpers, NotFoundError

import pprint

def get_indices(es, ym, no):
    index_name = "test.{}.*.*.{}".format(ym, no)
    result = es.indices.get(index=index_name, ignore_unavailable=True)
    return list(result.keys())

def delete(es):
    query = {
        "query": {
            "bool": {
                "should": [
                    {
                        "bool": {
                            "must": [
                                {
                                    "term": {
                                        "name": "jiro0"
                                    }
                                },
                                {
                                    "term": {
                                        "age": 25
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "bool": {
                            "must": [
                                {
                                    "term": {
                                        "name": "jiro1"
                                    }
                                },
                                {
                                    "term": {
                                        "age": 26
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
    #r = es.search(index="students*", body=query, ignore_unavailable=True)
    r = es.delete_by_query(index="students*", body=query, ignore_unavailable=True)
    pprint.pprint(r)

# 問題
# Elasticsearch id でしか更新できない
# 項目の組み合わせで更新するには、まず削除して、データを投入する
# ただし、パフォーマンスが著しく悪そう
# 同じデータが投入されてもよいか？
# 回避方法？
# td-agentがElasticsearch id を項目からのハッシュで作っているかもしれない
# id値を項目からのハッシュで作っているならば何もしなくても、更新される

es = Elasticsearch("http://localhost:9200")
#r = get_indices(es, "202202", "0001")
#print(r)
delete(es)
