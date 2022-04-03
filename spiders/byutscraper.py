import scrapy

class byutspider(scrapy.Spider):
    name='byut'
    start_urls=['https://www.bayut.com/to-rent/property/dubai/',
       
        
        ]
    def __init__(self):
        url='https://www.bayut.com/to-rent/property/dubai/page-'

        for page in range(1,3):
            self.start_urls.append(url + str(page))
        print(self.start_urls)    



    # base_url='https://www.bayut.com/to-rent/property/dubai/'

    def parse(self,response):
        for link in response.css('div._4041eb80 a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_properties)

        # net_page_partil_url= response.css('a.b7880daf ').attrib['href']
        # next_page_url=self.base_url+net_page_partil_url
        # yield scrapy.Request(next_page_url,callback=self.parse)

        
    def parse_properties(self,response):  
        products =response.css('div._6803f627')
        for product in products:
            yield{
                'one to 5':products.css('span._812aa185::text').getall(),
                'price': products.css('span._105b8a67 ::text').get(),
                'currency': products.css('span.e63a6bfb ::text').get(),
                'location':products.css('div._1f0f1758::text').get(),
                'bed_bath_size':products.css('span.cfe8d274 ::text').getall(),
                'permit':products.css('span.ff863316::text').getall(),  
                'agent name': products.css('span._55e4cba0::text').get(),
                'breadcrumbs':response.css('span._327a3afc ::text').getall(),
                'amentities':products.css('span._005a682a::text').getall(),
                'image_url':products.css('img::attr(src)').get(),
                'description':products.css('span._2a806e1e::text').getall(),
                
            }
          
        # next_page= response.css('a.b7880daf ').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)