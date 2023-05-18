from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
