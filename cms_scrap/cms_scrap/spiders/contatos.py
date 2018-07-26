# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from cms_scrap.items import Contato

import scrapy

class ContatosSpider(scrapy.Spider):

    name = 'contatos'
    allowed_domains = ['cms.ba.gov.br']
    start_urls = ['http://www.cms.ba.gov.br/vereadores_contatos.aspx/']
    download_delay = 1.5

    def parse(self, response):

        try:
            
            if response.status == 404:

                self.append(self.bad_log_file, response.url)
            
            if response.status == 200:

                table = response.xpath('//table[@id="zebra_table"]')
                trs = table.xpath('./tr') 
                del trs [:1]

                for tds in trs:
                    #Parse contatos
                    l = ItemLoader (item=Contato(), selector=tds)
                    l.add_xpath('vereador', './td[1]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('gabinete', './td[2]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('telefone', './td[3]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('email', './td[4]/text()'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('partido', './td[5]/text()'.encode('utf-8'), MapCompose(str.strip))

                    yield l.load_item()  
            else:

                self.append(self.bad_log_file, response.url)      

        except Exception:

            self.log('[exception] : %s' % e)

         
