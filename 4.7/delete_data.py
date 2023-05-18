from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
result = es.delete(index='news', id='1')
print(result)
