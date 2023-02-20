# Professor HeidelTime

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

Create a multilingual corpus weakly labeled with [HeidelTime](https://github.com/HeidelTime/heideltime).

## Source Corpus

We run the weak labeling for six languages. The details of the corpus for each language are described below.

| Dataset                 | Language | #Docs     | From       | To          | #Tokens per doc | #Annotations | 
|-------------------------|----------|-----------|------------|-------------|-----------------|--------------|
| [All the News 2.0]      | EN       | 24,642    | 2016-01-01 | 2020-04-02  | 18,755,616      | 254,803      |
| [Italian Crime News]    | IT       | 9,619     | 2011-01-01 | 2021-12-31  | 3,296,898       | 58,823       |
| [ElMundo News]          | ES       | 33,266    | 2003-01-01 | 2022-12-31  | 21,617,888      | 348,011      |
| [German News Dataset]   | DE       | 19,095    | 2005-12-02 | 2021-10-18  | 12,515,410      | 194,043      |
| [French Financial News] | FR       | 27,154    | 2017-10-19 | 2021-03-19  | 1,673,053       | 83,431       |
| [Público News]          | PT       | 24,293    | 2000-11-14 | 2002-03-20  | 5,929,377       | 111,810      |

Dataset: ph_spanish
Number of documents: 33266
Number of tokens: 21617888
Number of timexs: 348011
---------------------------

[All the News 2.0]: https://components.one/datasets/all-the-news-2-news-articles-dataset/

[Italian Crime News]: https://github.com/federicarollo/Italian-Crime-News

[ElMundo News]: https://github.com/hmosousa/elmundo_scraper

[German News Dataset]: https://www.kaggle.com/datasets/pqbsbk/german-news-dataset

[French Financial News]: https://www.kaggle.com/datasets/arcticgiant/french-financial-news

[Público News]: https://drive.inesctec.pt/s/N4ETjmF4k2MNkEs/download/publico_news.zip

## Run Annotations

### Setup development environment

```shell
virtualenv venv --python=python3.10
source venv/bin/activate
pip install -r requirements.txt
```

To assert that everything is working run pytest: `python -m pytest tests`

### Download data

```shell
sh data/download.sh
```

### Run the annotation

```shell
python -m src.run --language english
```

## Meta

[Hugo Sousa](https://hugosousa.net) - hugo.o.sousa@inesctec.pt

This framework is part of the [Text2Story](https://text2story.inesctec.pt) project which is financed by the ERDF – European Regional Development Fund through the North Portugal Regional Operational Programme (NORTE 2020), under the PORTUGAL 2020 and by National Funds through the Portuguese funding agency, FCT - Fundação para a Ciência e a Tecnologia within project PTDC/CCI-COM/31857/2017 (NORTE-01-0145-FEDER-03185)
