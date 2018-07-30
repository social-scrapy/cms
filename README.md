# Social Scrapy

Este projeto tem como objetivo o compartilhamento de informações e o desenvolvimento de soluções voltadas à colet/análise de dados públicos disponibilizados pela Câmara Municipal de Salvador a partir da utilização do framework [Scrapy](https://scrapy.org/).

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

* Despesas - Coleta as informações da URL http://www.cms.ba.gov.br/despesa.aspx referentes às dispesas dos vereadores com viagens. Este Spider 
trata da criação de requisições Posts (ASP.net) que visam a paginação da referida URL.
* Contatos - Coleta as informações da URL http://www.cms.ba.gov.br/vereadores_contatos.aspx relacionadas aos contatos dos vereadores.
* Vereadores - Coleta as informações da URL http://www.cms.ba.gov.br/vereadores.aspx, inclusive as imagens listadas na citada URL. Ainda em relação a este Spider, vale ressaltar que foi utilizado o Pipeline 'scrapy.pipelines.images.ImagesPipeline' na raspagem das imagens que compôem a citada lista.

### Execução Spiders

No diretório data, executar:
```
scrapy crawl <spider> -o <file>.<csv/json>
```



