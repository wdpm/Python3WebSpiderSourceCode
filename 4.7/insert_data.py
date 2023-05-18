from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
es.indices.create(index='news', ignore=400)

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
}
result = es.create(index='news', id=2, body=data)
print(result)
# {'_index': 'news', '_type': '_doc', '_id': '2', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
