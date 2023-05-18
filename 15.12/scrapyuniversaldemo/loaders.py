from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Identity, Compose


class MovieItemLoader(ItemLoader):
    # take first get the first non-empty value in list
    # 这是所有字段的默认处理函数，如果某些字段需要特殊处理，应该覆盖这个行为
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)
