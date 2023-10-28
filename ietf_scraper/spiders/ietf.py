import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        # title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author = response.xpath('//span[@class = "author-name"]/text()').get()
        auth_co = response.xpath('//span[@class="author-company"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        auth_add = response.xpath('//span[@class="address"]/text()').get()
        auth_ph = response.xpath('//span[@class="phone"]/text()').get()
        subHeading = response.xpath('//span[@class="subheading"]/text()').getall() # to get data from the text use text()
        desc = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get() # to get all data from tag use @tag_name 
        return {
            "title" : title,
            "author" : author,
            "author company" : auth_co,
            "date" : date,
            "Auth Add" : auth_add,
            "Auth Phone" : auth_ph,
            "SubHeading" : subHeading,
            "Description" : desc
            }
