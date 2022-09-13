# Professor HeidelTime

Create a multilingual corpus weakly labeled by [HeidelTime](https://github.com/HeidelTime/heideltime).

## Source Corpus

We run the weak labeling for six languages. The details of the corpus for each language are described below.

| Dataset                 | Language | #Docs     | Date Span                 | #Tokens per doc | #Annotations | 
|-------------------------|----------|-----------|---------------------------|-----------------|--------------|
| [All the News 2.0]      | EN       | 2,688,878 | 2016-01-01 to 2020-04-02  |                 |              |
| [Italian Crime News]    | IT       |           | 2011 to 2021              |                 |              |
| [ElMundo News]          | ES       |           | 2003-01-01 to 2022        |                 |              |
| [German News Dataset]   | DE       | 162,991   |                           |                 |              |
| [French Financial News] | FR       | 41,531    | 2017-10-19 to 2022        |                 |              |
| [110-PT-BN-KP]          | PT       | 110       | 2000-10-09 to 2000-10-09  |                 |              |

[All the News 2.0]: https://components.one/datasets/all-the-news-2-news-articles-dataset/
[Italian Crime News]: https://github.com/federicarollo/Italian-Crime-News
[ElMundo News]: https://github.com/hmosousa/elmundo_scraper
[German News Dataset]: https://www.kaggle.com/datasets/pqbsbk/german-news-dataset
[French Financial News]: https://www.kaggle.com/datasets/arcticgiant/french-financial-news
[110-PT-BN-KP]: https://github.com/LIAAD/KeywordExtractor-Datasets/blob/master/datasets/110-PT-BN-KP.zip

## Run Annotations

### Setup development environment

```shell
virtaulenv venv --python=python3.8
source venv/bin/python activate
pip install -r requirements.txt
```

### Install HeidelTime

For this project, we used the [py_heideltime](https://github.com/JMendes1995/py_heideltime) which requires some steps for
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
