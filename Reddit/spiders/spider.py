import scrapy
from ..items import RedditItem

class Reddit(scrapy.Spider):

    name = "reddit"
    start_urls = [
        "https://www.reddit.com/"
    ]

    def parse(self,response):
        all_reddits = response.css("._11R7M_VOgKO1RJyRSRErT3")
        print(len(all_reddits))
        items = RedditItem()
        for reddit in all_reddits:
            title = reddit.css("._eYtD2XCVieq6emjKBH3m::text").extract()
            link = reddit.css("div.SQnoC3ObvgnGjWt90zD9Z::text").extract()
            
            items["title"] = title
            items["link"] = link
            yield items