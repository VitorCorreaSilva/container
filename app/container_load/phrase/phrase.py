from container_load.phrase.conf import *
from container_load import api

class PhraseDAO(object):
    def __init__(self):
        self.counter = 0
        self.phrases = []

    def get(self, id):
        for phrase in self.phrases:
            if phrase['id'] == id:
                return phrase
        api.abort(404, "Frase {} não existe".format(id))

    def create(self, data):
        phrase = data
        phrase['id'] = self.counter = self.counter + 1
        self.phrases.append(phrase)
        return phrase

    def update(self, id, data):
        phrase = self.get(id)
        phrase.update(data)
        return phrase

    def delete(self, id):
        phrase = self.get(id)
        self.phrases.remove(phrase)
