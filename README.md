# Professor HeidelTime
[![Paper](https://img.shields.io/badge/Paper-557C55)](https://dl.acm.org/doi/10.1145/3583780.3615130)
[![DOI](https://zenodo.org/badge/doi/10.57967/hf/0897.svg)](doi.org/10.57967/hf/0897)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![Download](https://img.shields.io/badge/-download-9cf)](https://drive.inesctec.pt/s/B4JojTJaMyR8wDN/download/professor_heideltime.zip)


Professor HeidelTime is a project to create a multilingual corpus weakly labeled with [HeidelTime](https://github.com/HeidelTime/heideltime), a temporal tagger.

## Getting Started

### Download the Annotated Data

To download the Professor HeidelTime corpus, click on the following link: [Professor HeidelTime corpus](https://drive.inesctec.pt/s/B4JojTJaMyR8wDN/download/professor_heideltime.zip).

The downloaded archive contains six folders, each representing a different language. Inside each folder, there is one `.json` file for each annotated news article. The English, Italian, German, and French files contain `text`, `dct`, and `timexs` keys. However, due to licensing issues, the Portuguese and Spanish corpus files currently lack the `text` key. We are actively working with news sources to license these datasets for redistribution.

In the meantime, you can access the texts by running the following scrapping scripts: [Spanish](https://github.com/hmosousa/elmundo_scraper) and [Portuguese](https://github.com/hmosousa/publico_scraper).

### Corpus Details

The weak labeling was performed in six languages. Here are the specifics of the corpus for each language:

| Dataset                 | Language | Documents | From       | To         | Tokens     | Timexs    |
| ----------------------- | -------- | --------- | ---------- | ---------- | ---------- | --------  |
| [All the News 2.0]      | EN       | 24,642    | 2016-01-01 | 2020-04-02 | 18,755,616 | 254,803   |
| [Italian Crime News]    | IT       | 9,619     | 2011-01-01 | 2021-12-31 | 3,296,898  | 58,823    |
| [ElMundo News]          | ES       | 33,266    | 2003-01-01 | 2022-12-31 | 21,617,888 | 348,011   |
| [German News Dataset]   | DE       | 19,095    | 2005-12-02 | 2021-10-18 | 12,515,410 | 194,043   |
| [French Financial News] | FR       | 27,154    | 2017-10-19 | 2021-03-19 | 1,673,053  | 83,431    |
| [Público News]          | PT       | 24,293    | 2000-11-14 | 2002-03-20 | 5,929,377  | 111,810   |

## Running Annotations

### Set up Development Environment

To start with, set up a virtual environment and activate it. Then, install the necessary packages from the requirements file:

```shell
virtualenv venv --python=python3.10
source venv/bin/activate
pip install -r requirements.txt
```

Run pytest to ensure that everything is working correctly: `python -m pytest tests`

### Kaggle API Key

To add the Kaggle API keys to your machine, follow the instructions provided on [kaggle-api](https://github.com/Kaggle/kaggle-api).

### Download Raw Data

You can download the raw data by executing the following command:

```shell
sh data/download.sh
```

### Execute the Annotation

To run the annotation, use the following command (replace 'english' with the language you want to annotate):

```shell
python src/run.py --language english
```

## Contact

For more information, reach out to [Hugo Sousa](https://hugosousa.net) at <hugo.o.sousa@inesctec.pt>.

This framework is a part of the [Text2Story](https://text2story.inesctec.pt) project. This project is financed by the ERDF – European Regional Development Fund through the North Portugal Regional Operational Programme (NORTE 2020), under the PORTUGAL 2020 and by National Funds through the Portuguese funding agency, FCT - Fundação para a Ciência e a Tecnologia within project PTDC/CCI-COM/31857/2017 (NORTE-01-0145-FEDER-03185).

## Cite

If you use this work, please cite the following [paper](https://dl.acm.org/doi/10.1145/3583780.3615130):

```bibtex
@inproceedings{10.1145/3583780.3615130,
    author = {Sousa, Hugo and Campos, Ricardo and Jorge, Al\'{\i}pio},
    title = {TEI2GO: A Multilingual Approach for Fast Temporal Expression Identification},
    year = {2023},
    isbn = {9798400701245},
    publisher = {Association for Computing Machinery},
    url = {https://doi.org/10.1145/3583780.3615130},
    doi = {10.1145/3583780.3615130},
    booktitle = {Proceedings of the 32nd ACM International Conference on Information and Knowledge Management},
    pages = {5401–5406},
    numpages = {6},
    keywords = {temporal expression identification, multilingual corpus, weak label},
    location = {Birmingham, United Kingdom},
    series = {CIKM '23}
}
```
