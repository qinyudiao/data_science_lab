from scrapy import Spider
from scrapy.selector import Selector
from paper import PapercrawlerItem
import pdfminer
import urllib.request
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice


class ICMLCrawler(Spider):
    name = "ICMLCrawler"
    start_urls = ["http://proceedings.mlr.press/v70/",]
    prefix = r"C:\Users\chrom\Documents\HW\data sci\lab3\files"
    allowed_domains = ["proceedings.mlr.press"]
    def parse(self, response):
        ##this isn't great formatting but i've already downloaded the files so now i'm just going to be messing with them
        ##this part of the file is the code that i used to download files but won't be using to parse them
        
        papers = Selector(response).xpath('//*[@id="content"]/div/div[@class="paper"]')

        titles = Selector(response).xpath('//*[@id="content"]/div/div[@class="paper"]/p[1]')
        paper_url = Selector(response).xpath('//*[@id="content"]/div/div[@class="paper"]/p[3]/a[2]')
        
        for title, pdf, sup in zip(titles, papers, paper_url):
            item = PapercrawlerItem()
            item['title'] = title.xpath('text()').extract()[0]
            
            item['url'] = sup.xpath('@href').extract()[0]
            
            file_url = response.css('.downloadline::attr(href)').get()
            file_url = response.urljoin(file_url)
            
            path = item['url'].split('/')[-1]
            
            urllib.request.urlretrieve(item['url'], r"C:/Users/chrom/Documents/HW/data sci/lab3/files/" + path)
            yield item