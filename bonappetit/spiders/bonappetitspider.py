from scrapy.spiders import Spider
from scrapy.selector import Selector
from bonappetit.items import BonappetitItem

#  'title'   : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[1]/h3/text()').extract(),
#           'ingredients' : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[2]/div[1]/div/ul/li/span/span[3]/text()').extract(),  
#           'prep' : response.xpath('//*[@id="recipe-ingredients"]/div[2]/div[3]/div[2]/div/ul/li[1]/div/text()').extract()
#      

class RecipeeSpider(Spider):
	name = "bonappetit"
	allowed_domains = ["bonappetit.com"]
	# start_urls = ["http://http://www.bonappetit.com/recipes/"]
	start_urls = ["http://www.bonappetit.com/recipe/passover-chocolate-toffee-matzo"]

	def parse(self, response):
		hxs = Selector(response)
		print response
		item = BonappetitItem()
		items = []
		item["title"] = response.url
		item["prep"] = hxs.xpath('//*[@id="recipe-ingredients"]/div[2]/div[3]/div[2]/div/ul/li[1]/div/text()').extract()		
		item["ingredients"] = hxs.xpath('//*[@id="recipe-ingredients"]/div[2]/div[2]/div[1]/div/ul/li/span/span[3]/text()').extract()
		items.append(item)
		return item
		
	