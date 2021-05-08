import json

class Config:
    def __init__(self):
        self.__config = {}
        with open('config.json') as f:
            self.__config = json.loads(f.read())
    
    def get(self, key):
        try:
            return self.__config[key]
        except:
            return None