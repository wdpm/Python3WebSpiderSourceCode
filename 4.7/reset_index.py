from elasticsearch import Elasticsearch

# install elasticsearch-analysis-ik plugin
# bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.13.2/elasticsearch-analysis-ik-7.13.2.zip
# ./bin/elasticsearch-plugin install file:///root/elasticsearch-analysis-ik-7.15.0.zip => work

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

# 在给mapping设置时只给了'title'字段一个text类型，而没有对'url'字段进行设置，所以Elasticsearch默认将其识别为keyword类型。
# 您可以在mapping中明确指定'url'字段的类型为text类型，并指定相应的analyzer和search_analyzer。
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
es.indices.put_mapping(index='news', body=mapping)
