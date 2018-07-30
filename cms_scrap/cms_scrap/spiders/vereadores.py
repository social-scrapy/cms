# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from cms_scrap.items import Vereador
from urllib.parse import urljoin
from PIL import Image

import scrapy

class VereadoresSpider(scrapy.Spider):
    
    name = 'vereadores'
    allowed_domains = ['cms.ba.gov.br']
    start_urls = ['http://www.cms.ba.gov.br/vereadores.aspx/']
    download_delay = 1.5

    def parse(self, response):

        try:
            
            if response.status == 404:

                self.append(self.bad_log_file, response.url)

            elif response.status == 200:

                selectors = response.xpath('//*[@class="lista-de-vereadores"]/li')
                             
                for lis in selectors:
                    
                    #Parse vereadores
                    l = ItemLoader (item=Vereador(), selector=lis)
                  
                    try:
                       
                        l.add_value('image_urls', urljoin("http://www.cms.ba.gov.br/", lis.xpath('./div[@class="foto-vereador"]/a/img/@src').extract_first()))

                    except IndexError:

                        self.append(self.bad_log_file, response.url)
			
                    l.add_xpath('nome', './div[@class="dados"]/span[@class="nome"]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('partido', './div[@class="dados"]/span[@class="partido"]/text()'.encode('utf-8'), MapCompose(str.strip))
                    yield l.load_item()  
        
            else:

                self.append(self.bad_log_file, response.url)

        except Exception as e:

            self.log('[exception] : %s' % e)
