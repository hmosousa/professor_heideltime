# Professor HeidelTime

Create a multilingual corpus weakly labeled with [HeidelTime](https://github.com/HeidelTime/heideltime).

## Source Corpus

We run the weak labeling for six languages. The details of the corpus for each language are described below.

| Dataset                 | Language | #Docs     | From       | To          | #Tokens per doc | #Annotations | 
|-------------------------|----------|-----------|------------|-------------|-----------------|--------------|
| [All the News 2.0]      | EN       | 2,688,878 | 2016-01-01 | 2020-04-02  |                 |              |
| [Italian Crime News]    | IT       | 10,395    | 2011-01-01 | 2021-12-31  |                 |              |
| [ElMundo News]          | ES       | 2,639,152 | 2003-01-01 | 2022-12-31  |                 |              |
| [German News Dataset]   | DE       | 174,915   | 2005-12-02 | 2021-10-18  |                 |
| [French Financial News] | FR       | 41,543    | 2017-10-19 | 2021-03-19  |                 |              |
| [Público News]          | PT       | 38,729    | 2000-11-14 | 2002-03-20  |                 |              |

[All the News 2.0]: https://components.one/datasets/all-the-news-2-news-articles-dataset/

[Italian Crime News]: https://github.com/federicarollo/Italian-Crime-News

[ElMundo News]: https://github.com/hmosousa/elmundo_scraper

[German News Dataset]: https://www.kaggle.com/datasets/pqbsbk/german-news-dataset

[French Financial News]: https://www.kaggle.com/datasets/arcticgiant/french-financial-news

[Público News]: https://drive.inesctec.pt/s/N4ETjmF4k2MNkEs/download/publico_news.zip

## Run Annotations

### Setup development environment

```shell
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

### Install HeidelTime

For this project, we used the [py_heideltime](https://github.com/JMendes1995/py_heideltime) which requires some steps
for
the installation that is dependent on the OS. Please follow the
[installation instructions](https://github.com/JMendes1995/py_heideltime#option-2-standalone-installation) on
`py_heideltime` repo.

For Linux systems, the installation is reduced to providing HeidelTime tree tagger execution permission. This can be
accomplished with the following script.

```shell
sudo chmod 111 venv/lib/python3.8/site-packages/py_heideltime/Heideltime/TreeTaggerLinux/bin/*
```

### Download data

```shell
sh data/download.sh
```

### Run the annotation

```shell
python -m src.run --data_path "data/raw/english/data.csv" --language "english" --n_files_annotate 10000 --output_path "data/annotated/english"
```
