from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news_articles


#views
@main.route("/")
def index():
    """
    View root page that returns the index page and its data
    """
    #getting news
    general_news = get_news("general")
    
    return render_template("index.html", general = general_news) 



@main.route('/articles/<id>')
def articles(id):
    '''
    View article function that returns the articles in a source
    '''
    articles = get_news_articles(id)
    return render_template('articles.html', id = id, articles = articles)