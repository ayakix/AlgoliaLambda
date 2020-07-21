from chalice import Chalice, Response
from algoliasearch.search_client import SearchClient
from jinja2 import Environment, FileSystemLoader

import os
import jinja2
import urllib.parse

app = Chalice(app_name='algolia')

@app.route('/')
def index():
    context = {'message': ''}
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '.'), encoding='utf8'))
    template = env.get_template('index.html')
    html = template.render()
    return Response(html, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})

@app.route('/stations/{station}')
def stations(station):
    client = SearchClient.create(os.environ["ALGOLIA_PROJECT_ID"], os.environ["ALGOLIA_API_KEY"])
    clientIndex = client.init_index('station')
    return clientIndex.search(urllib.parse.unquote(station))
