# Social Scrapy

Este projeto tem como objetivo o compartilhamento de informações e o desenvolvimento de soluções voltadas à coleta/análise de dados públicos disponibilizados pela Câmara Municipal de Salvador a partir da utilização do framework [Scrapy](https://scrapy.org/).

## Pré-Requisitos

### Instalação PIP

```
sudo apt install python3-pip
```

### Instalação Virtualenv
```
sudo pip3 install virtualenv 
```

### Ciação do ambiente Virtualenv
```
virtualenv venv
```

### Ativação do ambiente Virtualenv
```
source venv/bin/activate
```

## Spiders Desenvolvidos

* Despesas - http://www.cms.ba.gov.br/despesa.aspx - Raspagem dos dados referentes às dispesas dos vereadores com viagens. Vale destacar que este spider trata da criação de requisições Posts (ASP.net) que visam a paginação da referida página.
* Contatos - http://www.cms.ba.gov.br/vereadores_contatos.aspx - Raspagem dos dados relacionadas aos contatos dos vereadores.
* Vereadores - http://www.cms.ba.gov.br/vereadores.aspx - Raspagem dos dados de cada vereador, inclusive, as imagens dos mesmos. Para a extração das imagens foi utilizado o Pipeline 'scrapy.pipelines.images.ImagesPipeline'.
### Execução Spiders

No diretório data, executar:
```
scrapy crawl <spider> -o <file>.<csv/json>
```



