from scrapy.spider import BaseSpider
from scrapy.select import HtmlXPathSelector
from bonappetit.items import BonappetitItem

#  'title'   : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[1]/h3/text()').extract(),
#           'ingredients' : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[2]/div[1]/div/ul/li/span/span[3]/text()').extract(),  
#           'prep' : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[3]/div[2]/div/ul/li[1]/div/text()').extract()
#      

class RecipeeSpider(BaseSpider):
	name = "BonAppetit"
	allowed_domains = ["bonappetit.com"]
	# start_urls = ["http://http://www.bonappetit.com/recipes/"]
	start_urls = ['http://www.bonappetit.com/recipe/passover-chocolate-toffee-matzo']
	items = []
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		