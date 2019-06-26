# -*- coding: utf-8 -*-

####
# Spider to crawl FACADatabase.gov
# References:
# - scrapy documentation: https://docs.scrapy.org/en/latest/intro/overview.html
# - xpaths: https://devhints.io/xpath
# - other1: https://stackoverflow.com/questions/52091790/making-scrapy-spider-follow-links-in-given-starting-url
# - other2: https://stackoverflow.com/questions/40479789/how-to-scrape-all-the-content-of-each-link-with-scrapy
###
from scrapy.spiders import CrawlSpider, Rule
from faca_scraper.items import FACAScraperItem
from scrapy.linkextractors import LinkExtractor


class FACASpider(CrawlSpider):
    name = 'facaspider'
    allowed_domains = ['facadatabase.gov']
    start_urls = ['https://www.facadatabase.gov/FACA/apex/FACAPublicAgencyNavigation']
    # rule gets links from index page of committees, follows each committee link
    # and calls the parse_committees method to scrape the information
    rules = (
             Rule(LinkExtractor(
                restrict_xpaths=("//div[@class='aircraft-section']//a"),
                deny=('(Reports)', )),
                callback='parse_committees',
                follow=True
                 ),
            )

    def parse_committees(self, response):
        '''
        Parses each committee's information and stores it into a FACAScraperItem
        '''
        item = FACAScraperItem()
        name_agency = response.xpath("//td[@class='dataCol  first ']/span/text()").extract()
        item['url_from'] = self.start_urls[0]
        item['url_to'] = response.url
        item['agency'] = name_agency[1]
        item['name'] = name_agency[0]
        item['committee_url'] = response.xpath("//td[@class='dataCol ']//a/@href").extract()[0]
        item['status'] = response.xpath("//td[@class='dataCol ']/span/text()").extract()[3]

        yield item


"""
    def parse_contents(self, response):
        '''
        Parses each committee FACA page
        '''
        items = []
        output = response.xpath("//div[@class='aircraft-section']//a/@href").extract()
        committee_lst = [link for link in links_all if 'Reports' not in link]
        for committee in committee_lst:
            url = urljoin(start_urls[0], p)
            r =

    # visit all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        '''
        Parses through the Committee list and singles out the relevant links
        '''
        committees = []
        output = response.xpath("//div[@class='aircraft-section']//a/@href").extract()
        committee_lst = [link for link in links_all if 'Reports' not in link]
        for committee in committee_lst:
            url = urljoin(start_urls[0], p)
            yield scrapy.Request(url, callback=self.parse_contents)

        item = FACAScraperItem()
        item['url_from'] = url
        item['url_to'] =

        yield item


            url_from = scrapy.Field()
            # The destination URL
            url_to = scrapy.Field()
            # agency name
            agency = scrapy.Field()
            # committee name
            committee = scrapy.Field()
            # committee url
            committee_url = scrapy.Field()

            if is_allowed:
                item = EPAScraperItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)

        response.xpath("//td[@class='dataCol ']//a/@href").extract()[0]
"""
