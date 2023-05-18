from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
if es.ping():
    print('Connected to Elasticsearch')
else:
    print('Could not connect to Elasticsearch')

result = es.indices.create(index='news',)
# result = es.indices.create(index='news', ignore=400)
print(result)
