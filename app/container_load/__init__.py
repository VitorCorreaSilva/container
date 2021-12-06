from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x11R\xdd?G\x02|\xdfD\xc5\xcb\xad\xcc\xa2\xf0\xca\xdes&\xd0\x05\xc2\xbfF'
app.config['ERROR_404_HELP'] = False

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Frases API',
    description='Uma API simples para salvar frases',
)
health_namespace = api.namespace('health', "Verifica a saúde do serviço.")
load_namespace = api.namespace('phrases', description='Conjunto de funções para carregar, deletar, criar e editar frases')

phrase = api.model('Frase', {
    'id': fields.Integer(readonly=True, description='O identificador da frase'),
    'text': fields.String(required=True, description='A frase que foi digitada')
})

from container_load import routes
