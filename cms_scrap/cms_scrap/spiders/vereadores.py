# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from cms_scrap.items import Vereador

import scrapy
import urlparse

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
                    image_urls = response.url
                    try:
                        image_urls = urlparse.urljoin(response.url, lis.xpath('./div[@class="foto-vereador"]/a/img/@src'.encode('utf-8')).extract())
                        l.add_xpath('image_urls', [x for x in image_urls])
                    except IndexError:
                        l.add_xpath('image_urls', image_urls)
                    l.add_xpath('foto', './div[@class="foto-vereador"]/a/img/@src'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('nome', './div[@class="dados"]/span[@class="nome"]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('partido', './div[@class="dados"]/span[@class="partido"]/text()'.encode('utf-8'), MapCompose(str.strip))
                    yield l.load_item()  
        
            else:

                self.append(self.bad_log_file, response.url)

        except Exception as e:

            self.log('[exception] : %s' % e)
