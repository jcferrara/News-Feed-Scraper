import feedparser # pip install feedparser
import pandas as pd  

feeds = {
        'The Economist': "https://www.economist.com/united-states/rss.xml",
        'New York Times': "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
        'Wall Street Journal': "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
        'Reuters': "http://feeds.reuters.com/Reuters/worldNews",
        'City Lab': "https://www.citylab.com/feeds/posts/",
        'TechCrunch': "http://feeds.feedburner.com/TechCrunch/startups"
        }

def get_daily_news(sources):
    
    """
    PARAMETERS
    ----------
    sources: Accepts a dictionary with rss urls as values. For example, {'The Economist': 'https://www.economist.com/united-states/rss.xml'}
    
    RETURNS
    ----------
    data: pd.DataFrame with columns title, published_date, summary, source, id
    
    REQUIRES
    ----------
    import feedparser
    import pandas as pd
    
    """
    
    feeds = sources
    
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
    daily_data.drop_duplicates(subset=['id'], inplace = True)
    
    return(daily_data)