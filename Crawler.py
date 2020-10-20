import crawler
from crawler.ArticleFetcher import ArticleFetcher
fetcher = ArticleFetcher()
counter = 0
for article in fetcher.fetch():
    if counter == 10:
        break
    counter += 1
    print(article.emoji + " : " + article.title)
