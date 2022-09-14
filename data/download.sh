
mkdir data/raw/
cd data/raw/

echo "Downloading English corpus."
wget -q --show-progress https://www.dropbox.com/s/cn2utnr5ipathhh/all-the-news-2-1.zip
unzip -d english all-the-news-2-1.zip
rm all-the-news-2-1.zip
mv  english/all-the-news-2-1.csv english/data.csv

echo "Downloading Italian corpus."
mkdir italian
cd italian
wget -q --show-progress https://raw.githubusercontent.com/hmosousa/Italian-Crime-News/main/italian_crime_news.csv
mv italian_crime_news.csv data.csv
cd ..

echo "Downloading German corpus."
kaggle datasets download -d pqbsbk/german-news-dataset
unzip -d german german-news-dataset.zip
rm german-news-dataset.zip

echo "Downloading French corpus."
kaggle datasets download -d arcticgiant/french-financial-news
unzip -d french french-financial-news.zip
rm french-financial-news.zip
rm french/FrenchNewsDayConcat.csv
mv french/FrenchNews.csv french/data.csv

echo "Downloading Portuguese corpus."
wget -q --show-progress https://drive.inesctec.pt/s/N4ETjmF4k2MNkEs/download/publico_news.zip
unzip -d portuguese publico_news.zip
rm publico_news.zip
mv portuguese/publico portuguese/data

echo "Downloading Spanish corpus."
wget -q --show-progress https://drive.inesctec.pt/s/CjBZsGRBn6qxGd2/download/elmundo_news.zip
unzip -d spanish elmundo_news.zip
rm elmundo_news.zip

cd ../..
