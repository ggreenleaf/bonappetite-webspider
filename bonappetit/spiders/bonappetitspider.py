# from scrapy.spiders import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from bonappetit.items import BonappetitItem

class RecipeeSpider(CrawlSpider):
	name = "bonappetit"
	allowed_domains = ["bonappetit.com"]
	start_urls = ["http://www.bonappetit.com/sitemap/recipes"]
	
	rules = (
		Rule(LinkExtractor(restrict_xpaths='//*[@id="wrapper"]/div/div/div/section/div/div[2]/a')), #next button of sitemap/recipes
		Rule(LinkExtractor(restrict_xpaths='//*[@id="wrapper"]/div/div/div/section/div/li/a'),callback="parse_recipe") #the recipe page we need to scrap
		)
	

	def parse_recipe(self, response):
		hxs = Selector(response)
		item = BonappetitItem()
		item["url"] = response.url
		item["name"] = hxs.xpath('//*[@id="content-header-wrapper"]/div[1]/h1/text()').extract()
		item["prep"] = hxs.xpath('//li[contains(@class, "step")]/div/text()').extract()		
		item["ingredients"] = hxs.xpath('//*[@id="recipe-ingredients"]/div[2]/div[2]/div[1]/div/ul/li/span/span[3]/text()').extract()
		
		yield item
	# def parse_recipee_list(self, response):
	# 	hxs = Selector(response)
			
		
	