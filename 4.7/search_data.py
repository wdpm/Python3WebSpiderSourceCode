from elasticsearch import Elasticsearch
import json

# OR
dsl = {
    'query': {
        'match': {
            'title': '高考 圆梦'
        }
    }
}

# AND
# dsl = {
#     'query': {
#         'bool': {
#             'must': [
#                 {'match': {'title': '高考'}},
#                 {'match': {'title': '圆梦'}}
#             ]
#         }
#     }
# }

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
result = es.search(index='news', body=dsl)
# print(json.dumps(result, indent=2, ensure_ascii=False))
print(result)

# {'took': 297, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 4, 'relation': 'eq'}, 'max_score': 1.8518889, 'hits': [{'_index': 'news', '_type': '_doc', '_id': '6oRj6ocBEG--E6QQsviK', '_score': 1.8518889, '_source': {'title': '乘风破浪不负韶华，奋斗青春圆梦高考', 'url': 'http://view.inews.qq.com/a/EDU2021041600732200'}}, {'_index': 'news', '_type': '_doc', '_id': '7oRk6ocBEG--E6QQ6_iW', '_score': 1.8518889, '_source': {'title': '乘风破浪不负韶华，奋斗青春圆梦高考', 'url': 'http://view.inews.qq.com/a/EDU2021041600732200'}}, {'_index': 'news', '_type': '_doc', '_id': '6IRj6ocBEG--E6QQsvgM', '_score': 0.81085134, '_source': {'title': '高考结局大不同', 'url': 'https://k.sina.com.cn/article_7571064628_1c3454734001011lz9.html'}}, {'_index': 'news', '_type': '_doc', '_id': '7IRk6ocBEG--E6QQ6_gY', '_score': 0.81085134, '_source': {'title': '高考结局大不同', 'url': 'https://k.sina.com.cn/article_7571064628_1c3454734001011lz9.html'}}]}}

result = es.search(index='news')
print(result)
# print(json.dumps(result, indent=2, ensure_ascii=False))
