import pickle
import pandas
from gnews import GNews
# import beautifulsoup
import csv

google_news = GNews(max_results=3)
news_dict = dict()
cities = pandas.read_csv("worldcities.csv").set_index('city').T.to_dict('list')
for city in cities:
    news_dict[city] = ""
    req = google_news.get_news_by_location(city)
    for i in range(min(len(req), 3)):
        news_pop_up = '<a href=' + req[i]['url'] + ">" + str(i + 1) + '.' + \
                      req[i]['title'] + '</a>'
        news_dict[city] += news_pop_up + '\n'

f = open("daily_news.pkl", "wb")
pickle.dump(news_dict, f)
f.close()
