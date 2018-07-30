# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CmsScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Contato(scrapy.Item):
    vereador = Field()
    gabinete = Field()
    telefone = Field()
    email = Field()
    partido = Field()
    pass

class Despesa(scrapy.Item):
    data = Field()
    tipo = Field()
    responsavel = Field()
    usuario = Field()
    valor = Field()
    localidade = Field()
    justificativa = Field()
    pass

class Vereador(scrapy.Item):
    nome = Field()
    partido = Field()
    image_urls = Field()
    images = Field()
    pass
