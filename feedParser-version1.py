#feed Parser

import feedparser
#import speedparser
#from speedparser import parse
import atom
import requests

feedurl="https://timesofindia.indiatimes.com/rssfeedstopstories.cms?x=2"


CleanUrls=["http://timesofindia.indiatimes.com/rssfeedstopstories.cms?x=1","http://www.thehindu.com/news/national/?service=rss","http://www.business-standard.com/rss/latest.rss","http://www.dnaindia.com/syndication/rss,catid-2.xml","http://www.oneindia.com/rss/news-india-fb.xml","http://feeds.feedburner.com/ScrollinArticles.rss","http://www.financialexpress.com/feed","http://www.thehindubusinessline.com/?service=rss"]


for i in range(len(CleanUrls)):

    print(CleanUrls[i])

    #response = requests.get(CleanUrls[i])
    feed = feedparser.parse(CleanUrls[i])
    
    for i in feed.entries:
    #    print(i)
        print("Title: "+i.title)
        print("Description:  "+ i.description)
        print("Published Date: "+i.published[5:-6])
        print("\n\n")
        title = i.title
        description = i.description
        date = i.published[5:-6]
       
