import scrapy


class MemberspiderSpider(scrapy.Spider):
    name = "memberspider"
    allowed_domains = ["www.sfma.org.sg"]
    start_urls = ["https://www.sfma.org.sg/member/members-directory"]

    def parse(self, response):
        company_list=response.xpath('//div[@class="list-group"]/a/@href').getall()
        for company in company_list:
            #main_page_url='https://www.sfma.org.sg/member/members-directory'
            company_info_page_url='https://www.sfma.org.sg/member/'+ company
            yield response.follow(company_info_page_url,callback=self.parse_company_info_page)

    def parse_company_info_page(self,response):

        yield{
            'company_name':response.xpath('//strong/h6/text()').get(),
            'company_address':response.xpath('normalize-space(//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[1])').get(),
            'telephone':response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[3]/text()').get(),
            'fax':response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[4]/text()').get(),
            'mail':response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[5]/text()').get(),
            'website':response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[6]/text()').get(),
            'company_desc':response.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/child::p[7]/text()').get(),
        }
        
