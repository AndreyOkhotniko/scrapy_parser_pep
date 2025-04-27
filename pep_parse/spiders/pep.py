import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_page_links = response.css('a[href^="pep-"]::attr(href)').getall()
        for pep_link in pep_page_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        the_title = response.css('h1.page-title::text').get()
        number = the_title.split()[1]
        name = the_title.split(' – ', 1)[-1].strip()
        status = response.css('abbr::text').get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
