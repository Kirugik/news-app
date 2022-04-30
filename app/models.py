class Source:
    '''
    Source class to define news sources objects
    '''

    def __init__(self, id, name, url, category):
        self.id = id
        self.name = name
        self.url = url
        self.category = category


class Article:
    '''
    Article class to define news article objects
    '''

    def __init__(self, id, title, description, url, image, timePublished):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.timePublished = timePublished 