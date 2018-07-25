# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from cms_scrap.items import Despesa
from scrapy.http import Request
from w3lib.html import remove_tags

import datetime
import socket
import scrapy

class CmsSpider(scrapy.Spider):

    name = 'despesas'
    allowed_domains = ['cms.ba.gov.br']
    start_urls = ['http://www.cms.ba.gov.br/despesa.aspx/']
    download_delay = 1.5

    def parse(self, response):

        try:
            if response.status == 404:
                self.append(self.bad_log_file, response.url)

            elif response.status == 200:
                selectors = response.xpath('//*[@id="ContentPlaceHolder1_UpdatePanel1"]/div')
                del selectors[:2]
                del selectors[-1]
                
                for divs in selectors:
                    #parse despesas
                    l = ItemLoader (item=Despesa(), selector=divs)
                    l.add_xpath('data', './b[contains(text(),"Data")]/following-sibling::text()[1]'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('tipo', './b[contains(text(),"Tipo")]/following-sibling::text()[1]'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('responsavel', u'./b[contains(text(),"Responsável")]/following-sibling::text()[1]', MapCompose(str.strip))
                    l.add_xpath('usuario', './b[contains(text(),"Usuário")]/following-sibling::text()[1]', MapCompose(str.strip))
                    l.add_xpath('valor', './b[contains(text(),"Valor")]/following-sibling::text()[1]'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('localidade', './b[contains(text(),"Localidade")]/following-sibling::text()[1]'.encode('utf-8'), MapCompose(str.strip))
                    l.add_xpath('justificativa', './b[contains(text(),"Justificativa")]/following-sibling::text()[1]'.encode('utf-8'), MapCompose(str.strip, remove_tags), Join())
                    yield l.load_item()          
            else:
                self.append(self.bad_log_file, response.url)

        except Exception as e:
            self.log('[exception] : %s' % e)
        
        #pagination post request
        yield scrapy.FormRequest.from_response(
            response,
            url="http://www.cms.ba.gov.br/despesa.aspx/",
            formdata = {                  
                '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00',
                'ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00' : 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00'
            },
            callback = self.parse
        )

      

    
    


