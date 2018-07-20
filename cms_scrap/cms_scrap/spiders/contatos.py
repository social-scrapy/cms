# -*- coding: utf-8 -*-
import scrapy

from cms.items import Contato

class ContatosSpider(scrapy.Spider):
    name = 'contatos'
    allowed_domains = ['cms.ba.gov.br']
    start_urls = ['http://www.cms.ba.gov.br/vereadores_contatos.aspx/']
    download_delay = 1.5

    def parse(self, response):
        try:
            if response.status == 200:
                table = response.xpath('//table[@id="zebra_table"]')
                trs = table.xpath('./tr') 
                del trs [:1]
                for tds in trs:
                    contato = Contato()
                    contato['vereador'] = tds.xpath('./td[1]/text()').extract()
                    contato['gabinete'] = tds.xpath('./td[2]/text()').extract()
                    contato['telefone'] = tds.xpath('./td[3]/text()').extract()
                    contato['email'] = tds.xpath('./td[4]/text()').extract()
                    contato['partido'] = tds.xpath('./td[5]/text()').extract()
                    yield contato
                    
        except Exception:
            self.log('[exception] : %s' % e)

         
