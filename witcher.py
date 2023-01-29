import scrapy

class Witcher(scrapy.Spider):
    name='witcher'
    start_urls = ['https://witcher.fandom.com/wiki/Category:The_Witcher_characters']

    def parse(self,response):
        
        linki = list()
        for link in response.css('a.category-page__member-link'):
            linki.append(link.attrib['href'])
        yield from response.follow_all(linki, self.parseCharacter)
        
    def parseCharacter(self,response):
        try:
            yield{
                'name':response.css('h1.page-header__title::text').extract_first(),
                'race':response.css('div[data-source=Race]').extract_first(),
                'gender':response.css('div[data-source=Gender]').extract_first()
            }
        except:
            yield{
                'name':'',
                'race':'',
                'gender':''
            }