from flask import render_template
from . import main
from ..requests import get_sources, get_articles
from ..models import Source, Article


@main.route('/')
def index():
    """ 
    View root page function that returns the index page and its data 
    """
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainement')
    general_news = get_sources('general')
    health_news = get_sources('politics')
    science_news = get_sources('science')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')

    title = 'Home - Welcome to All News Sources'
    
    return render_template('index.html', title=title,business=business_news,entertainment=entertainment_news,general=general_news,health=health_news,science=science_news,sports=sports_news,technology=technology_news)


@main.route('/articles/<id>')
def articles(id):
    """  
    View function to display articles from different sources
    """
    articles = get_articles(id)
    title = f'{id}'
    return render_template('news.html',title=title,articles=articles)