# Task 69 - Beautiful soup

import feedparser

NewsFeed = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
print("Listing latest 10 news articles..")

for i in range(10):
    entry = NewsFeed.entries[i]

    print(entry['title'])
