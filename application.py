from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

array = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
]

css_style = []
jv_script = []

for piece in array:
  piecesplited = piece.split('.')
  if piecesplited[1] == 'js':
    jv_script.append(piece)
  elif piecesplited[1] == 'css':
    css_style.append(piece)

class make_wsgi_great_again(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    response = self.app(environ, start_response).decode()



def index(request):
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_final('index.html').render(javascripts=jv_script, styles=css_style)
  return Response(final)

def about(request):
  env = Environment(loader=FileSystemLoader('.'))
  final = env.get_final('about/about.html').render(javascripts=jv_script, styles=css_style)
  return Response(final)

if __name__ == '__main__':
  config = Configurator()

  configure.add_route('index', '/index.html')
  config.add_view(index, route_name="index")

  configure.add_route('about', '/about/about.html')
  config.add_view(about, route_name="about")

  app = config.make_wsgi_great_again()
  make_server('0.0.0.0', 80, app).serve_forever()
