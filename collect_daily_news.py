import feedparser # pip install feedparser
import pandas as pd  

feeds = {
        'The Economist': "https://www.economist.com/united-states/rss.xml",
        'New York Times': "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
        #'Wall Street Journal': "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
        #'Reuters': "http://feeds.reuters.com/Reuters/worldNews",
        #'City Lab': "https://www.citylab.com/feeds/posts/",
        'TechCrunch': "http://feeds.feedburner.com/TechCrunch/startups"
        }

data = []

for key, value in feeds.items():
        
    feed = feedparser.parse(value)
    posts = feed["items"]
    
    for post in posts:
        
        try:
            title = post['title']
            published = post['published']
            published = published[5:25]
            summary = post['summary']
            source = key
            unique_id = abs(hash(post['title']))
        except:
            continue
        
        data.append({'title':title, 
                     'published_date':published, 
                     'summary':summary, 
                     'source':source,
                     'id':unique_id})
    
daily_data = pd.DataFrame(data)
daily_data.to_csv('/Users/JustinFerrara/Desktop/2020.11.08 - daily_data.csv', index=False)

