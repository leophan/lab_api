from sqlalchemy import create_engine, engine

class DB:
    
    def __init__(self, url):
        self._url = url


    def connect(self):
        engine = create_engine(self._url, echo=False)
        return engine
