# -*- coding: utf-8 -*-
import scrapy

from cms_scrap.items import Despesa
from scrapy.http import Request

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

                divs_despesas = response.xpath('//*[@id="ContentPlaceHolder1_UpdatePanel1"]/div')
                del divs_despesas[:2]
                del divs_despesas[-1]

                for divs in divs_despesas:
                    despesa = Despesa()
                    despesa['data'] = divs.xpath('./b[contains(text(),"Data")]/following-sibling::text()[1]').extract()
                    despesa['tipo'] = divs.xpath('./b[contains(text(),"Tipo:")]/following-sibling::text()[1]').extract()
                    despesa['responsavel'] = divs.xpath('./b[contains(text(),"Responsável:")]/following-sibling::text()[1]').extract()
                    despesa['usuario'] = divs.xpath('./b[contains(text(),"Usuário:")]/following-sibling::text()[1]').extract()
                    despesa['valor'] = divs.xpath('./b[contains(text(),"Valor:")]/following-sibling::text()[1]').extract()
                    despesa['localidade'] = divs.xpath('./b[contains(text(),"Localidade:")]/following-sibling::text()[1]').extract()
                    despesa['justificativa'] = divs.xpath('./b[contains(text(),"Justificativa:")]/following-sibling::text()[1]').extract()
                    yield despesa

            else:
                self.append(self.bad_log_file, response.url)

        except Exception:
            self.log('[exception] : %s' % e)
        
        yield scrapy.FormRequest.from_response(
            response,
            url="http://www.cms.ba.gov.br/despesa.aspx/",
            formdata = {                  
                '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00',
                'ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00' : 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$dpNoticia$ctl02$ctl00'
            },
            callback = self.parse
        )
