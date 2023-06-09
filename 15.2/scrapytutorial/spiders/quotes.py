# -*- coding: utf-8 -*-
import scrapy

from scrapytutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # response 第一次是start_urls执行请求后的结果
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        # next_page
        next = response.css('.pager .next a::attr(href)').extract_first()
        if next:
            url = response.urljoin(next)
            yield scrapy.Request(url=url, callback=self.parse)
