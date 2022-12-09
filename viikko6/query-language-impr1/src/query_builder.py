from matchers import All


class QueryBuilder:
    def __init__(self, url):    
        self._url = url
    
    def build(self):
        return All()