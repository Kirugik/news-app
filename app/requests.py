import urllib.request,json
from .models import Source, Article

# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting news secondary url
secondary_url = None


def configure_request(app):
    global api_key, base_url, secondary_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    secondary_url = app.config['NEWS_API_SECONDARY_URL'] 


def get_sources(category):
    '''
    Function that gets the json response to the url request for news sources
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

    return source_results


def process_source_results(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain news details
    Returns :
        source_results: A list of news objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        category = source_item.get('category')
        
        if name:
            source_object = Source(id, name, url, category)
            source_results.append(source_object)

    return source_results


def get_articles(id):
    '''
    Function that gets the json response to the url request for news articles 
    '''
    get_articles_url = secondary_url.format(id, api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        article_results = None
        
        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_article_results(article_results_list)
        
    return article_results


def process_article_results(article_list):
    
    article_results = [] 
    
    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt') 
        
        if title:
            article_object = Article(id, title, description, url, urlToImage, publishedAt)
            article_results.append(article_object)

    return article_results
