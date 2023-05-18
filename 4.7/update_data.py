from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

data = {
    'doc': {
        'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
        'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
        'date': '2021-07-05'
    }
}
result = es.update(index='news', body=data, id=2)
print(result)

# {'_index': 'news', '_type': '_doc', '_id': '2', '_version': 2, 'result': 'updated', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 5, '_primary_term': 1}
# version bump