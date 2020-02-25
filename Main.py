import requests
url = 'http://172.17.50.43/halice'
r = requests.get(url)
print(r.text)
#Getting Status Code
print("Status Code:")
print("\t*",r.status_code)
#headers time
h = requests.head(url)
print("Header:")
print("**********")
# for line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# Modifying the User-Agent
headers = {
    'User-Agent': 'Mobile'
}
# Testing on another site
url2 = 'http://172.17.50.53/halice'
rh = requests.get(url2, headers=headers)
print(rh.text)

# End of Part 5

#Beginning of Part 6

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.17.50.43/halice']
    def parse(self, response):
        css_sel = 'img' #xpath sel = '//img'
        for x in response.css(css_sel):
    #   for x in response.xpath (xpath_sel):
            newsel = '@src'
            yield {
                'IMAGE link': x.xpath(newsel) .extract_first()
            }
        next_sel = '.next a::attr(href)'
        next_page = response.css(next_sel).extract_first()
        if next_page: #not last page
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

