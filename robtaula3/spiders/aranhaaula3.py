import scrapy
import os
import pathlib
import csv



class Aranhaaula3Spider(scrapy.Spider):
    name = 'aranhaaula3'
    #allowed_domains = ['del.com']
    start_urls = ['https://www.infomoney.com.br/tudo-sobre/acoes/']

    def parse(self, response):
        for caixadenoticias in response.css('.article-card__content'):
            yield{
            'Noticias': caixadenoticias.css('.article-card__headline::text').get()
            }
        pass
