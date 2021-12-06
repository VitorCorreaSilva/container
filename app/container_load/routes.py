from container_load import phrase, api
from container_load.phrase.phrase import *

from container_load import load_namespace, health_namespace
from flask_restx import Resource
from flask import request

DAO = PhraseDAO()

@health_namespace.route("")
class Health(Resource):
    def get(self):
        return {
            "online": True
        }

@load_namespace.route('/')
class PhraseList(Resource):
    @load_namespace.doc('list_phrases')
    @load_namespace.marshal_list_with(phrase)
    def get(self):
        return DAO.phrases

    @load_namespace.doc('create_phrase')
    @load_namespace.expect(phrase)
    @load_namespace.marshal_with(phrase, code=201)
    def post(self):
        return DAO.create(api.payload), 201


@load_namespace.route('/<int:id>')
@load_namespace.response(404, 'phrase not found')
@load_namespace.param('id', 'The phrase identifier')
class Phrase(Resource):
    @load_namespace.doc('get_phrase')
    @load_namespace.marshal_with(phrase)
    def get(self, id):
        return DAO.get(id)

    @load_namespace.doc('delete_phrase')
    @load_namespace.response(204, 'phrase deleted')
    def delete(self, id):
        DAO.delete(id)
        return '', 204

    @load_namespace.expect(phrase)
    @load_namespace.marshal_with(phrase)
    def put(self, id):
        return DAO.update(id, api.payload)